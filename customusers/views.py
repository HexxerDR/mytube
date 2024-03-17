from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import views as auth_views
from django.core.mail import send_mail

from django.dispatch import receiver
from django.db.models.signals import pre_save

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
        send_mail(instance.username, "Hello, click this link to activate your account http://127.0.0.1:8000/auth/activate/{}".format(instance.verToken), 'settings.EMAIL_HOST_USER', [instance.email])


def confirmEmail(request, verToken):
    userToActivate = CustomUser.objects.get(verToken=verToken)
    if userToActivate.is_active == False:
        userToActivate.is_active = True
        userToActivate.save()
        return redirect('mytube-base')
    if userToActivate.is_active == True:
        return redirect('mytube-base')