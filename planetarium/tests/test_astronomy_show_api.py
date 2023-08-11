from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from planetarium.models import AstronomyShow
from planetarium.serializers import (
    AstronomyShowListSerializer,
    AstronomyShowDetailSerializer,
)
from planetarium.tests.model_samples import (
    sample_astronomy_show,
    sample_show_theme,
)


ASTRONOMY_SHOW_URL = reverse("planetarium:astronomyshow-list")


class UnauthenticatedAstronomyShowApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_authenticate_required(self):
        response = self.client.get(ASTRONOMY_SHOW_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedAstronomyShowTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "testuser@test.com", "testpass123"
        )
        self.client.force_authenticate(self.user)

    def test_list_astronomy_shows(self):
        astronomy_show = sample_astronomy_show()
        show_themes = [sample_show_theme(i) for i in range(2)]
        astronomy_show.show_themes.set(show_themes)

        response = self.client.get(ASTRONOMY_SHOW_URL)

        astronomy_shows = AstronomyShow.objects.all()
        serializer = AstronomyShowListSerializer(astronomy_shows, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_astronomy_show_list_filter_by_title(self):
        astronomy_show1 = sample_astronomy_show(id=35123)
        astronomy_show2 = sample_astronomy_show(id=1954)
        astronomy_show3 = sample_astronomy_show(id=123)

        res = self.client.get(ASTRONOMY_SHOW_URL, {"title": "123"})

        serializer1 = AstronomyShowListSerializer(astronomy_show1)
        serializer2 = AstronomyShowListSerializer(astronomy_show2)
        serializer3 = AstronomyShowListSerializer(astronomy_show3)

        self.assertIn(serializer1.data, res.data)
        self.assertNotIn(serializer2.data, res.data)
        self.assertIn(serializer3.data, res.data)

    def test_astronomy_show_list_filter_by_show_themes(self):
        astronomy_show1 = sample_astronomy_show(id=35123)
        astronomy_show2 = sample_astronomy_show(id=1954)
        astronomy_show3 = sample_astronomy_show(id=123)

        show_theme1 = sample_show_theme(id=1)
        show_theme2 = sample_show_theme(id=2)
        show_theme3 = sample_show_theme(id=11111)

        astronomy_show1.show_themes.add(show_theme1)
        astronomy_show2.show_themes.add(show_theme2)
        astronomy_show3.show_themes.add(show_theme3)

        res = self.client.get(
            ASTRONOMY_SHOW_URL, {"show_themes": f"{show_theme2.id}"}
        )

        serializer1 = AstronomyShowListSerializer(astronomy_show1)
        serializer2 = AstronomyShowListSerializer(astronomy_show2)
        serializer3 = AstronomyShowListSerializer(astronomy_show3)
        self.assertNotIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)

    def test_retrieve_astronomy_show_detail(self):
        astronomy_show = sample_astronomy_show()
        show_theme = sample_show_theme()

        astronomy_show.show_themes.set([show_theme])

        url = reverse(
            "planetarium:astronomyshow-detail", args=[astronomy_show.id]
        )
        res = self.client.get(url)

        serializer = AstronomyShowDetailSerializer(astronomy_show)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_astronomy_show_create_forbidden(self):
        payload = {"name": "Sample Astronomy Show", "description": "TEST"}
        res = self.client.post(ASTRONOMY_SHOW_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminAstronomyShowApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="testuser@test.com", password="testpass123", is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_astronomy_show(self):
        show_theme = sample_show_theme()
        payload = {
            "title": "Sample Astronomy_show",
            "description": "TEST",
            "show_themes": [show_theme.id],
        }
        res = self.client.post(ASTRONOMY_SHOW_URL, payload)
        astronomy_show = AstronomyShow.objects.get(id=res.data["id"])

        astronomy_shows = AstronomyShow.objects.all()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn(astronomy_show, astronomy_shows)

    def test_delete_astronomy_show_not_allowed(self):
        astronomy_show = sample_astronomy_show()
        url = reverse(
            "planetarium:astronomyshow-detail", args=[astronomy_show.id]
        )

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
