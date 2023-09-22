from django.urls import path, include
from rest_framework import routers

from planetarium.views import (
    ShowThemeViewSet,
    ReservationViewSet,
    AstronomyShowViewSet,
    PlanetariumDomeViewSet,
    ShowSessionViewSet,
)


router = routers.DefaultRouter()
router.register("show_themes", ShowThemeViewSet)
router.register("reservations", ReservationViewSet)
router.register("astronomy_shows", AstronomyShowViewSet)
router.register("planetarium_domes", PlanetariumDomeViewSet)
router.register("show_sessions", ShowSessionViewSet)


urlpatterns = router.urls

app_name = "planetarium"
