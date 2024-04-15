from django.urls import path
from . import views

urlpatterns = [
    path('user/usersub/<str:verToken>', views.UserSubscribeProfile, name='user-subscribe'),
    path('user/video/<int:pk>/usersub/<str:verToken>', views.UserSubscribeVideo, name='uservid-subscribe')
]