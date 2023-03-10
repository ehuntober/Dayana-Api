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
    serializer_class = UserSerializer 
    
    def post(self,request):
        username= request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        
        if user is None:
            return Response({'detail': 'Invalid credentail'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not user.check_password(password):
            return Response({'detail': 'Invalid credentails'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access' : str(refresh.access_token),
        })
        
        