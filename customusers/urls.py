from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/", views.register, name="user-register"),
    path("login/", views.CustomLogin.as_view(template_name="customusers/login.html"), name="user-login"),
    path("logout/", views.CustomLogout.as_view(template_name="customusers/logout.html"), name="user-logout"),
    path("profile/<str:verToken>/videos", views.profileVideoView, name="mytube-userprofile-videos"),
    path("profile/<str:verToken>/community", views.profileCommView, name="mytube-userprofile-community"),
    path("profile/<str:verToken>/featured", views.profileFeatView, name="mytube-userprofile-featured"),
    path("profile/<str:verToken>/playlists", views.profilePlaylView, name="mytube-userprofile-playlists"),
    path("activate/<str:verToken>", views.confirmEmail, name="user-confirm"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

