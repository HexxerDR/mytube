# Generated by Django 5.0.3 on 2024-03-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0008_alter_video_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="created",
            field=models.IntegerField(default=0),
        ),
    ]