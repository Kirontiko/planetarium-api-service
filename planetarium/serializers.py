from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from planetarium.models import ShowTheme, Ticket


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ("id", "name", )
