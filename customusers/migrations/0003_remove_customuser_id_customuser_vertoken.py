# Generated by Django 5.0.3 on 2024-03-12 14:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customusers", "0002_alter_customuser_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="id",
        ),
        migrations.AddField(
            model_name="customuser",
            name="verToken",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
