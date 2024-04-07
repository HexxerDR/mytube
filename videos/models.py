from django.db import models
from customusers.models import CustomUser
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
import os, subprocess, uuid, time, shutil
from django.conf import settings

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

def uploadPath(instance, filename):
        if instance.author.verToken:
            upload_to = "videosuploads/{}/{}".format(slugify(instance.author.verToken), (instance.vidID))
        return os.path.join(upload_to, filename)

def randVidID():
    vidID = str(uuid.uuid4()) + str(time.time())
    return vidID

class Video(models.Model):
    videoemb = models.FileField(max_length=500, upload_to=uploadPath, null=False, validators=[FileExtensionValidator(allowed_extensions=["mov","mp4","avi","wmv"])])
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    vidID = models.CharField(default=randVidID, editable=False)
    ratingn = models.BigIntegerField(default = 0)
    ratingp = models.BigIntegerField(default = 0)
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(editable=False, max_length=255, default="image/image.png")
    created = models.IntegerField(editable=False, default=0)

    class Meta:
        ordering=['-created_at']


@receiver(post_save, sender=Video)
def vidThumbnailCreate(sender, instance, **kwargs):
    if instance.created == 0:
        if instance._state.adding is False:
            acPath = str(instance.id) + "-" + instance.vidID
            os.renames("media/videosuploads/{}/{}".format(slugify(instance.author.verToken), (instance.vidID)), "media/videosuploads/{}/{}".format(slugify(instance.author.verToken), (acPath)))
            thmDes = os.path.basename(str(instance.videoemb))
            thmBase, thmde = os.path.splitext(str(instance.videoemb))
            thmBase = os.path.basename(thmBase)
            vidpath = "media/videosuploads/{}/{}/{}".format(instance.author.verToken, acPath, thmDes)
            thmpath = "media/videosuploads/{}/{}/{}.png".format(instance.author.verToken, acPath, thmBase)
            process = subprocess.run(["ffmpeg", "-i", vidpath, "-ss", "00:00:01", "-vf", "thumbnail, scale=1920:1080", "-frames:v", "1", thmpath])
            instance.created += 1
            instance.videoemb = "videosuploads/{}/{}/{}".format(instance.author.verToken, acPath, thmDes)
            if os.path.isfile(thmpath):
                instance.thumbnail = "videosuploads/{}/{}/{}.png".format(instance.author.verToken, acPath, thmBase)
            else:
                instance.thumbnail = "default_thumbnail.png"
            instance.save()

@receiver(post_delete, sender=Video)
def vidThumbnailCreate(sender, instance, **kwargs):
    acPath = str(instance.id) + "-" + instance.vidID
    thmDes = os.path.basename(str(instance.videoemb))
    thmBase, thmde = os.path.splitext(str(instance.videoemb))
    thmBase = os.path.basename(thmBase)
    dirpath = "media/videosuploads/{}/{}".format(instance.author.verToken, acPath)
    shutil.rmtree(dirpath)