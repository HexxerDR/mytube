from django.shortcuts import render
from django.views.generic import DetailView
from .models import Video


class VideoDetail(DetailView):
    model = Video

