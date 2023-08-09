from django.urls import path, include
from rest_framework import routers

from planetarium.views import ShowThemeViewSet, ReservationViewSet, AstronomyShowViewSet, PlanetariumDomeViewSet

router = routers.DefaultRouter()
router.register("show_themes", ShowThemeViewSet)
router.register("resevations", ReservationViewSet)
router.register("astronomy_shows", AstronomyShowViewSet)
router.register("planetarium_domes", PlanetariumDomeViewSet)


urlpatterns = [
    path("", include(router.urls))
]

app_name = "planetarium"
