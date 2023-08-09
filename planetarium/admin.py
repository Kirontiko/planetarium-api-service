from django.contrib import admin

from planetarium.models import (ShowTheme,
                                Reservation,
                                PlanetariumDome,
                                Ticket,
                                AstronomyShow,
                                ShowSession)

admin.site.register(ShowTheme)
admin.site.register(Reservation)
admin.site.register(PlanetariumDome)
admin.site.register(AstronomyShow)
admin.site.register(Ticket)
admin.site.register(ShowSession)
