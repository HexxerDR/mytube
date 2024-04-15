from django.urls import path
from . import views

urlpatterns = [
    path('video/<int:pk>/dislike', views.VideoDislike, name='video-dislike')
]