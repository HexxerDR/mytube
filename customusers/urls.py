from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="user-register"),
    path("login/", views.CustomLogin.as_view(template_name="customusers/login.html"), name="user-login"),
    path("logout/", views.CustomLogout.as_view(template_name="customusers/logout.html"), name="user-logout"),
    path("profile/<str:verToken>", views.profileView, name="mytube-userprofile"),
    path("activate/<str:verToken>", views.confirmEmail, name="user-confirm"),
]

