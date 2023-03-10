

from django.shortcuts import render
from rest_framework import generics, permissions
from api.custom_renderers import JPEGRenderer, PNGRenderer
from rest_framework.response import Response
from images.models import Images



# *** import  the apis 
from rest_framework.response import Response 
from rest_farmework.parsers import FileUploadParser 
from django.shortcuts import get_objects_or_404 
from .serializers import ImageSerializer


class ImageAPIView(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        queryset = Images.objects.get(id=self.kwargs['id'][:2]).image
        data = queryset
        return Response(data, content_type='image/jpeg')


class ListImage(generics.ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

