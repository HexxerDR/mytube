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
                send_mail(username, "Hello", 'settings.EMAIL_HOST_USER', [form.cleaned_data.get('email')])
                messages.success(request, f"{username}, your account has been created!")
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
def user_nactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        print("Creating Inactive User")
        instance.is_active = False
    else:
        print("Updating User Record")