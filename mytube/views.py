from django.shortcuts import render#, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
#from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.urls import reverse_lazy
#from django import forms
#from rest_framework.decorators import api_view
#from rest_framework.response import Response

#from rest_framework import status
#from rest_framework.authtoken.models import Token
from customusers.models import CustomUser
from videos.models import Video


class MytubeBaseView(ListView):
    model = CustomUser

def profileView(request, verToken):
    userToView = CustomUser.objects.get(verToken=verToken)
    userVideos = Video.objects.get(author=userToView)
    return render(request, "customusers/profile.html", {"userToView":userToView, "userVideos":userVideos})