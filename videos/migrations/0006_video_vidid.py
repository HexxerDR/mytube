# Generated by Django 5.0.3 on 2024-03-21 09:53

import videos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0005_alter_video_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="vidID",
            field=models.CharField(default=videos.models.randVidID, editable=False),
        ),
    ]
