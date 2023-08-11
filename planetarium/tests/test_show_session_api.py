import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from planetarium.models import ShowSession
from planetarium.serializers import (
    ShowSessionListSerializer,
    ShowSessionDetailSerializer,
)
from planetarium.tests.model_samples import (
    sample_astronomy_show,
    sample_show_theme,
    sample_show_session,
    sample_planetarium_dome,
)

SHOW_SESSION_URL = reverse("planetarium:showsession-list")


class UnauthenticatedAstronomyShowApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_authenticate_required(self):
        response = self.client.get(SHOW_SESSION_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedAstronomyShowTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "testuser@test.com", "testpass123"
        )
        self.client.force_authenticate(self.user)

    def test_list_show_sessions(self):
        sample_show_session()

        response = self.client.get(SHOW_SESSION_URL)

        show_sessions = ShowSession.objects.all()
        serializer = ShowSessionListSerializer(show_sessions, many=True)
        for data in response.data:
            del data["tickets_available"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_show_session_list_filter_by_date(self):
        show_time1 = (
            timezone.now().astimezone(timezone.get_current_timezone())
            + timezone.timedelta(days=10)
        ).isoformat()
        show_time2 = (
            timezone.now().astimezone(timezone.get_current_timezone())
            + timezone.timedelta(days=9)
        ).isoformat()
        show_time3 = (
            timezone.now().astimezone(timezone.get_current_timezone())
            + timezone.timedelta(days=2)
        ).isoformat()
        today = datetime.date.today()
        date_to_filter = today + datetime.timedelta(days=2)
        date_to_filter = date_to_filter.strftime("%Y-%m-%d")

        show_session1 = sample_show_session(show_time=show_time1)
        show_session2 = sample_show_session(show_time=show_time2)
        show_session3 = sample_show_session(show_time=show_time3)

        res = self.client.get(SHOW_SESSION_URL, {"date": date_to_filter})

        serializer1 = ShowSessionListSerializer(show_session1)
        serializer2 = ShowSessionListSerializer(show_session2)
        serializer3 = ShowSessionListSerializer(show_session3)

        for data in res.data:
            del data["tickets_available"]

        self.assertNotIn(serializer1.data, res.data)
        self.assertNotIn(serializer2.data, res.data)
        self.assertIn(serializer3.data, res.data)

    def test_show_session_list_filter_by_astronomy_show(self):
        show_session1 = sample_show_session(
            astronomy_show=sample_astronomy_show(title="Yeeees Filter")
        )
        show_session2 = sample_show_session(
            astronomy_show=sample_astronomy_show(title="Not Yet Filtered")
        )
        show_session3 = sample_show_session(
            astronomy_show=sample_astronomy_show(title="Yes Filter")
        )
        astronomy_show1 = show_session1.astronomy_show.id
        res = self.client.get(
            SHOW_SESSION_URL, {"astronomy_show": f"{astronomy_show1}"}
        )

        serializer1 = ShowSessionListSerializer(show_session1)
        serializer2 = ShowSessionListSerializer(show_session2)
        serializer3 = ShowSessionListSerializer(show_session3)

        for data in res.data:
            del data["tickets_available"]

        self.assertIn(serializer1.data, res.data)
        self.assertNotIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)

    def test_retrieve_show_session_detail(self):
        show_session = sample_show_session()

        url = reverse("planetarium:showsession-detail", args=[show_session.id])
        res = self.client.get(url)

        serializer = ShowSessionDetailSerializer(show_session)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_show_session_create_forbidden(self):
        payload = {
            "show_time": timezone.now().astimezone(
                timezone.get_current_timezone()
            )
            + timezone.timedelta(days=10),
            "astronomy_show": sample_astronomy_show(),
            "planetarium_dome": sample_planetarium_dome(),
        }
        res = self.client.post(SHOW_SESSION_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminAstronomyShowApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="testuser@test.com", password="testpass123", is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_astronomy_show(self):
        astronomy_show = sample_astronomy_show()
        planetarium_dome = sample_planetarium_dome()
        payload = {
            "show_time": timezone.now().astimezone(
                timezone.get_current_timezone()
            )
            + timezone.timedelta(days=10),
            "astronomy_show": astronomy_show.id,
            "planetarium_dome": planetarium_dome.id,
        }
        res = self.client.post(SHOW_SESSION_URL, payload)
        show_session = ShowSession.objects.get(id=res.data["id"])

        show_sessions = ShowSession.objects.all()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn(show_session, show_sessions)

    def test_delete_show_session(self):
        show_session = sample_show_session()
        url = reverse("planetarium:showsession-detail", args=[show_session.id])

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
