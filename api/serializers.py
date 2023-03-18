
from rest_framework import serializers 
from images.models import Images

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id','category','title','alt','image','slug','created','author','status']
        
       