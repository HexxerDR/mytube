from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from . import models
from customusers.models import CustomUser
from videos.models import Video

@login_required()
def UserSubscribeProfile(request, verToken):
    subscribeduser = CustomUser.objects.get(verToken=verToken)
    subscribinguser = request.user
    subscribed = models.Subscriber.objects.filter(subscribing_user=subscribinguser, subscribed_user=subscribeduser)
    current_subscribers = subscribeduser.subscriberstotal
    if not subscribed and subscribinguser != subscribeduser:
        subscribed = models.Subscriber.objects.create(subscribing_user=subscribinguser, subscribed_user=subscribeduser)
        current_subscribers += 1
    elif subscribed and subscribinguser != subscribeduser:
        subscribed = models.Subscriber.objects.filter(subscribing_user=subscribinguser, subscribed_user=subscribeduser).delete()
        current_subscribers -= 1
    subscribeduser.subscriberstotal = current_subscribers
    subscribeduser.save()

    return HttpResponseRedirect(reverse('mytube-userprofile', args=[verToken]))

@login_required()
def UserSubscribeVideo(request, verToken, pk):
    subscribeduser = CustomUser.objects.get(verToken=verToken)
    vidsub = Video.objects.get(id=pk)
    subscribinguser = request.user
    subscribed = models.Subscriber.objects.filter(subscribing_user=subscribinguser, subscribed_user=subscribeduser)
    current_subscribers = subscribeduser.subscriberstotal
    if not subscribed and subscribinguser != subscribeduser:
        subscribed = models.Subscriber.objects.create(subscribing_user=subscribinguser, subscribed_user=subscribeduser)
        current_subscribers += 1
    elif subscribed and subscribinguser != subscribeduser:
        subscribed = models.Subscriber.objects.filter(subscribing_user=subscribinguser, subscribed_user=subscribeduser).delete()
        current_subscribers -= 1
    subscribeduser.subscriberstotal = current_subscribers
    subscribeduser.save()

    return HttpResponseRedirect(reverse('video-view', args=[pk]))