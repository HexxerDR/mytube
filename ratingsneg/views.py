from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from . import models
from comments.models import Comment
from videos.models import Video
from ratingspos.models import Ratingpos
# Create your views here.

@login_required()
def VideoDislike(request, pk):
    video = Video.objects.get(id=pk)
    user = request.user
    current_dislikes = video.ratingn
    current_likes = video.ratingp
    disliked = models.Ratingneg.objects.filter(rating_user=user, rated_video=video)
    liked = Ratingpos.objects.filter(rating_user=user, rated_video=video)
    if not liked and not disliked:
        disliked = models.Ratingneg.objects.create(rating_user=user, rated_video=video)
        current_dislikes += 1
    elif liked :
       disliked = models.Ratingneg.objects.create(rating_user=user, rated_video=video)
       liked = Ratingpos.objects.filter(rating_user=user, rated_video=video).delete()
       current_likes -= 1
       current_dislikes += 1
    elif disliked:
        disliked = models.Ratingneg.objects.filter(rating_user=user, rated_video=video).delete()
        current_dislikes -= 1
    
    video.ratingp = current_likes
    video.ratingn = current_dislikes
    video.save()

    return HttpResponseRedirect(reverse('video-view', args=[pk]))