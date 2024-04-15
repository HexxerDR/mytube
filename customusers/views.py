from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import views as auth_views
from django.core.mail import send_mail
from django.views.generic import DetailView

from django.dispatch import receiver
from django.db.models.signals import pre_save
from videos.models import Video
from pinnedvideos.models import PinnedVideo

from . import forms



def register(request):
    user = request.user
    if not user.is_authenticated:
        if request.method == "POST":
            form = forms.UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"{username}, your account has been created! An Email has been sent to you with an activation link!")
                return redirect('user-login')
        else:
            form = forms.UserRegisterForm()
        return render(request, 'customusers/register.html', {'form': form})
    else:
        return redirect('mytube-base')


class CustomLogin(UserPassesTestMixin, auth_views.LoginView):
    model = CustomUser

    def test_func(self):
        return not self.request.user.is_authenticated
    
class CustomLogout(LoginRequiredMixin, auth_views.LogoutView):
    model = CustomUser

@receiver(pre_save, sender=CustomUser)
def user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        instance.is_active = False
        send_mail(instance.username, "Hello, click this link to activate your account http://127.0.0.1:8000/user/activate/{}".format(instance.verToken), 'settings.EMAIL_HOST_USER', [instance.email])


def confirmEmail(request, verToken):
    userToActivate = CustomUser.objects.get(verToken=verToken)
    if userToActivate.is_active == False:
        userToActivate.is_active = True
        userToActivate.save()
        return redirect('mytube-base')
    if userToActivate.is_active == True:
        return redirect('mytube-base')

def profileVideoView(request, verToken):
    userToView = CustomUser.objects.get(verToken=verToken)
    
    if Video.objects.filter(author=userToView).exists():
        userVideos = Video.objects.filter(author=userToView)
        vidCount = userVideos.count
        return render(request, "customusers/profile_videos.html", {"userToView":userToView, "userVideos":userVideos, "vidCount":vidCount})
    else:
        return render(request, "customusers/profile_videos.html", {"userToView":userToView})
    
def profileCommView(request, verToken):
    userToView = CustomUser.objects.get(verToken=verToken)
    
    if Video.objects.filter(author=userToView).exists():
        userVideos = Video.objects.filter(author=userToView)
        vidCount = userVideos.count
        return render(request, "customusers/profile_community.html", {"userToView":userToView, "userVideos":userVideos, "vidCount":vidCount})
    else:
        return render(request, "customusers/profile_community.html", {"userToView":userToView})

def profileFeatView(request, verToken):
    userToView = CustomUser.objects.get(verToken=verToken)
    
    if Video.objects.filter(author=userToView).exists() and PinnedVideo.objects.filter(pinning_user=userToView):
        userVideos = Video.objects.filter(author=userToView)
        pinnedVideo = PinnedVideo.objects.get(pinning_user=userToView)
        vidCount = userVideos.count
        return render(request, "customusers/profile_featured.html", {"userToView":userToView, "userVideos":userVideos, "vidCount":vidCount, "pinnedVideo":pinnedVideo})
    elif Video.objects.filter(author=userToView).exists():
        userVideos = Video.objects.filter(author=userToView)
        vidCount = userVideos.count
        return render(request, "customusers/profile_featured.html", {"userToView":userToView, "userVideos":userVideos, "vidCount":vidCount})
    else:
        return render(request, "customusers/profile_featured.html", {"userToView":userToView})

def profilePlaylView(request, verToken):
    userToView = CustomUser.objects.get(verToken=verToken)
    
    if Video.objects.filter(author=userToView).exists():
        userVideos = Video.objects.filter(author=userToView)
        vidCount = userVideos.count
        return render(request, "customusers/profile_playlists.html", {"userToView":userToView, "userVideos":userVideos, "vidCount":vidCount})
    else:
        return render(request, "customusers/profile_playlists.html", {"userToView":userToView})

