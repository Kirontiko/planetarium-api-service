
from django.utils import timezone

from planetarium.models import ShowTheme, PlanetariumDome, AstronomyShow, ShowSession


def sample_show_theme(id=0):
    defaults = {
        "name": f"Sample Show Theme{id}",
    }

    return ShowTheme.objects.create(**defaults)


def sample_planetarium_dome(id=0):
    defaults = {
        "name": f"Sample Show Theme{id}",
        "rows": 1,
        "seats_in_row": 5
    }

    return PlanetariumDome.objects.get_or_create(**defaults)[0]


def sample_astronomy_show(id=0, **params):
    defaults = {
        "title": f"Sample Astronomy Show{id}",
        "description": "Sample Description",
    }
    defaults.update(params)

    return AstronomyShow.objects.get_or_create(**defaults)[0]


def sample_show_session(**params):
    defaults = {
        "show_time": timezone.now().astimezone(
            timezone.get_current_timezone()
        ) + timezone.timedelta(days=10),
        "astronomy_show": sample_astronomy_show(),
        "planetarium_dome": sample_planetarium_dome(),
    }
    defaults.update(params)

    return ShowSession.objects.create(**defaults)