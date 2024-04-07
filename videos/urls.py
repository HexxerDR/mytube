from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("<int:pk>/", views.VideoDetail.as_view(), name="video-view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

