# Generated by Django 5.0.3 on 2024-03-21 09:14

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customusers", "0004_alter_customuser_vertoken"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="verToken",
            field=models.TextField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
