from django.db import models
from customusers.models import CustomUser

from videos.models import Video

class Ratingneg(models.Model):
    rated_video = models.ForeignKey(Video, on_delete=models.CASCADE)
    rating_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)



