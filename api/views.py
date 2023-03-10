

from django.shortcuts import render
from rest_framework import generics, permissions
from api.custom_renderers import JPEGRenderer, PNGRenderer
from rest_framework.response import Response
from images.models import Images



# *** import  the apis 
from rest_framework.response import Response 
from rest_framework.parsers import FileUploadParser 
from django.shortcuts import get_object_or_404 
from .serializers import ImageSerializer
from rest_framework.decorators import api_view , APIView , permission_classes
from rest_framework.request import Request 
from rest_framework import status



class ImageAPIView(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        queryset = Images.objects.get(id=self.kwargs['id'][:2]).image
        data = queryset
        return Response(data, content_type='image/jpeg')


class ListImages(generics.ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    
class ImageDetail(generics.RetrieveAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    
class PersonalImages(generics.ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Images.objects.filter(author=self.request.user)
    
class PostImage(generics.CreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_class = (FileUploadParser,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        

# class DeleteImage(generics.DestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get_queryset(self):
#         return Images.objects.filter(author=self.request.user) 
    
#     def perform_destroy(self,instance):
#         instance.delete()
        
        
class UpdateImage(generics.UpdateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Images.objects.filter(author=self.request.user)
    

@api_view(http_method_names=['DELETE'])
def delete_image(request:Request,id:int):
    Image= get_object_or_404(Images,pk=id)
    
    Image.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    

