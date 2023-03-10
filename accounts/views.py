from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status 
from rest_framework.response import Response 
from rest_framework_simplejwt.tokens import RefreshToken 
from django.contrib.auth.models import User  
from .serializers import UserSerializer  


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    
class LoginAPIView(generics.GenericAPIView):
    serializer_class = User