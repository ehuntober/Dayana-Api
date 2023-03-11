
from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 
from .views import RegisterAPIView,login_view


urlpatterns = [
    path('register/',RegisterAPIView.as_view(),name='register'),
    # path('login/',LoginAPIView.as_view(),name='login'),
    path('login/',login_view, name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
