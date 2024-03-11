from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.MytubeBaseView.as_view(), name="mytube-base"),
    path("auth/", include("customusers.urls")),
]

