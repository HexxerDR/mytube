from django.shortcuts import render, get_object_or_404, redirect
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

def MyTubeSearchView(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searchedvid = Video.objects.filter(title__contains=searched)
        return render(request, "mytube/search.html", {'searched': searched, 'searchedvid': searchedvid})
    else:
        return render(request, "mytube/search.html", {})