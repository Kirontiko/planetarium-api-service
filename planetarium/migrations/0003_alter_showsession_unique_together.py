# Generated by Django 4.1 on 2023-08-09 18:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "planetarium",
            "0002_alter_reservation_options_alter_ticket_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="showsession",
            unique_together={
                ("astronomy_show", "planetarium_dome", "show_time")
            },
        ),
    ]
