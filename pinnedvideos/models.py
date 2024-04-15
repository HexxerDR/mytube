from django.db import models

from customusers.models import CustomUser
from videos.models import Video
from django.db.models import F, Q, CheckConstraint

class PinnedVideo(models.Model):
    pinned_video = models.OneToOneField(Video, on_delete=models.CASCADE)
    pinning_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name= "author", null=True)

    class Meta:
        constraints = [
            CheckConstraint(
                check = Q(pinning_user = F("author")),
                name = "user_and_video_author_same",
                )
        ]

