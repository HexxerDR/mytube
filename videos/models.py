from django.db import models
from customusers.models import CustomUser
from django.utils.text import slugify
import os

def uploadPath(instance, filename):
        if instance.author.verToken:
            upload_to = 'videosuploads/{}/{}'.format(slugify(instance.author.verToken), (instance.title))
        return os.path.join(upload_to, filename)


class Video(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    videoemb = models.FileField(upload_to=uploadPath, null=False)
    ratingn = models.BigIntegerField(default = 0)
    ratingp = models.BigIntegerField(default = 0)
    title = models.CharField(max_length=100)
