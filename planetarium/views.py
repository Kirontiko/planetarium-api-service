from django.shortcuts import render
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin,
                                   CreateModelMixin)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from planetarium.models import ShowTheme, Reservation, AstronomyShow, PlanetariumDome
from planetarium.permissions import IsAdminOrIfAuthenticatedReadOnly
from planetarium.serializers import (ShowThemeSerializer,
                                     ReservationListSerializer,
                                     ReservationSerializer,
                                     AstronomyShowDetailSerializer,
                                     AstronomyShowListSerializer,
                                     AstronomyShowSerializer, PlanetariumDomeSerializer)


class ShowThemeViewSet(CreateModelMixin,
                       ListModelMixin,
                       GenericViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class PlanetariumDomeViewSet(CreateModelMixin,
                             ListModelMixin,
                             GenericViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class ReservationPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class ReservationViewSet(ListModelMixin,
                         CreateModelMixin,
                         GenericViewSet, ):
    queryset = Reservation.objects.prefetch_related(
        "tickets__show_session__astronomy_show",
        "tickets__show_session__planetarium_dome"
    )
    serializer_class = ReservationSerializer
    pagination_class = ReservationPagination
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return ReservationListSerializer

        return ReservationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AstronomyShowViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    queryset = AstronomyShow.objects.prefetch_related("show_themes")
    serializer_class = AstronomyShowSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    @staticmethod
    def _params_to_ints(qs):
        """Converts a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        """Retrieve the movies with filters"""
        title = self.request.query_params.get("title")
        show_themes = self.request.query_params.get("show_themes")
        queryset = self.queryset
        if title:
            queryset = queryset.filter(title__icontains=title)
        if show_themes:
            genres_ids = self._params_to_ints(show_themes)
            queryset = queryset.filter(show_themes__id__in=genres_ids)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "list":
            return AstronomyShowListSerializer
        if self.action == "retrieve":
            return AstronomyShowDetailSerializer

        return AstronomyShowSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "show_themes",
                type={"type": "list", "items": {"type": "number"}},
                description="Filter by show_themes id (ex.?show_themes=1,2)",
                required=False
            ),
            OpenApiParameter(
                "title",
                type=str,
                description="Filter by title (ex.?title=Parade)",
                required=False
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


