from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Images 


class HomepageView(ListView):
    model = Images
    template_name = 'images/index.html'
    

class ImagesListView(ListView):
    model = Images
    template_name = 'images/all_image.html'
