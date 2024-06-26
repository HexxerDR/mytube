# Generated by Django 5.0.3 on 2024-03-31 14:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscriber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subscribed_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscribeduser_subscriber_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "subscribing_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscribinguser_subscriber_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
