from django.urls import path       

from .views import ImageAPIView , ListImages, ImageDetail , PersonalImages ,PostImage, DeleteImage ,UpdateImage
urlpatterns = [
    path('id/<id>',ImageAPIView.as_view()),
    path('images/',ListImages.as_view(),name='list-images'),
    path('images/<int:pk>/',ImageDetail.as_view(),name='image-detail'),
    path('images/personal/', PersonalImages.as_view(), name='personal-images'),
    path('images/upload/', PostImage.as_view(), name='post-image'),
    path('images/delete/<int:pk>/', DeleteImage.as_view(), name='delete-image'),
    path('images/<int:pk>/update/', UpdateImage.as_view(), name='update-image'),
    
]
