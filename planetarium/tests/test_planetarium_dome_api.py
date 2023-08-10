from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from planetarium.models import PlanetariumDome
from planetarium.serializers import PlanetariumDomeSerializer
from planetarium.tests.model_samples import sample_planetarium_dome

PLANETARIUM_DOME_URL = reverse("planetarium:planetariumdome-list")


class UnauthenticatedPlanetariumDomeApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_authenticate_required(self):
        response = self.client.get(PLANETARIUM_DOME_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedPlanetariumDomeTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "testuser@test.com",
            "testpass123"
        )
        self.client.force_authenticate(self.user)

    def test_list_planetarium_domes(self):
        sample_planetarium_dome()

        response = self.client.get(PLANETARIUM_DOME_URL)

        planetarium_domes = PlanetariumDome.objects.all()
        serializer = PlanetariumDomeSerializer(planetarium_domes, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_planetarium_dome_create_forbidden(self):
        payload = {
            "name": "Sample Planetarium Dome",
            "rows": 15,
            "seats_in_row": 5
        }
        res = self.client.post(PLANETARIUM_DOME_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminPlanetariumDomeApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="testuser@test.com",
            password="testpass123",
            is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_planetary_dome(self):
        payload = {
            "name": "Sample Dome",
            "rows": 10,
            "seats_in_row": 5
        }
        res = self.client.post(PLANETARIUM_DOME_URL, payload)
        planetarium_dome = PlanetariumDome.objects.get(id=res.data["id"])

        planetarium_domes = PlanetariumDome.objects.all()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn(planetarium_dome, planetarium_domes)