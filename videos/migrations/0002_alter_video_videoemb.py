# Generated by Django 5.0.3 on 2024-03-18 14:19

import videos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="videoemb",
            field=models.FileField(upload_to=videos.models.uploadPath),
        ),
    ]