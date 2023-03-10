from django.urls import path       

from .views import ImageAPIView , ListImages, ImageDetail , PersonalImages
urlpatterns = [
    path('id/<id>',ImageAPIView.as_view()),
    path('images/',ListImages.as_view(),name='list-images'),
    path('images/<int:pk>/',ImageDetail.as_view(),name='image-detail'),
    path('images/personal/', PersonalImages.as_view(), name='personal-images'),
    
]
