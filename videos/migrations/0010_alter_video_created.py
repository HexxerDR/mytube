# Generated by Django 5.0.3 on 2024-03-23 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0009_video_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="created",
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
