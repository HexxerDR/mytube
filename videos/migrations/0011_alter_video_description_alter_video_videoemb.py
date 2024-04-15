# Generated by Django 5.0.3 on 2024-03-24 11:26

import django.core.validators
import videos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0010_alter_video_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="description",
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name="video",
            name="videoemb",
            field=models.FileField(
                max_length=500,
                upload_to=videos.models.uploadPath,
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["mov", "mp4", "avi", "wmv"]
                    )
                ],
            ),
        ),
    ]