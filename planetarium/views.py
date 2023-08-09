from django.shortcuts import render
from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin, CreateModelMixin)
from rest_framework.viewsets import GenericViewSet

from planetarium.models import ShowTheme
from planetarium.serializers import ShowThemeSerializer


class ShowThemeViewSet(CreateModelMixin,
                       ListModelMixin,
                       GenericViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer
