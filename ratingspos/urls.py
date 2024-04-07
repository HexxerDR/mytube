from django.urls import path
from . import views

urlpatterns = [
    path('video/<int:pk>/like', views.VideoLike, name='video-like')
]