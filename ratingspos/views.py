from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from . import models
from comments.models import Comment
from videos.models import Video
from ratingsneg.models import Ratingneg
# Create your views here.

@login_required()
def VideoLike(request, pk):
    video = Video.objects.get(id=pk)
    user = request.user
    current_dislikes = video.ratingn
    current_likes = video.ratingp
    disliked = Ratingneg.objects.filter(rating_user=user, rated_video=video)
    liked = models.Ratingpos.objects.filter(rating_user=user, rated_video=video)
    if not liked and not disliked:
        liked = models.Ratingpos.objects.create(rating_user=user, rated_video=video)
        current_likes += 1
    elif disliked:
       liked = models.Ratingpos.objects.create(rating_user=user, rated_video=video)
       disliked = Ratingneg.objects.filter(rating_user=user, rated_video=video).delete()
       current_likes += 1
       current_dislikes -= 1
    elif liked:
        liked = models.Ratingpos.objects.filter(rating_user=user, rated_video=video).delete()
        current_likes -= 1
    video.ratingp = current_likes
    video.ratingn = current_dislikes
    video.save()

    return HttpResponseRedirect(reverse('video-view', args=[pk]))