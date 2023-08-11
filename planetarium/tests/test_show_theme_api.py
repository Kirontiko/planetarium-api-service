import datetime

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from planetarium.models import ShowTheme
from planetarium.serializers import ShowThemeSerializer
from planetarium.tests.model_samples import sample_show_theme


SHOW_THEME_URL = reverse("planetarium:showtheme-list")


class UnauthenticatedShowThemeApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_authenticate_required(self):
        response = self.client.get(SHOW_THEME_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedShowThemeTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "testuser@test.com", "testpass123"
        )
        self.client.force_authenticate(self.user)

    def test_list_show_themes(self):
        sample_show_theme()

        response = self.client.get(SHOW_THEME_URL)

        show_themes = ShowTheme.objects.all()
        serializer = ShowThemeSerializer(show_themes, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_show_theme_create_forbidden(self):
        payload = {
            "name": "Sample Theme",
        }
        res = self.client.post(SHOW_THEME_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminShowThemeApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="testuser@test.com", password="testpass123", is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_show_theme(self):
        payload = {
            "name": "Sample Theme",
        }
        res = self.client.post(SHOW_THEME_URL, payload)
        show_theme = ShowTheme.objects.get(id=res.data["id"])

        show_themes = ShowTheme.objects.all()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn(show_theme, show_themes)
