from django.urls import path       

from .views import ImageAPIView
urlpatterns = [
    path('id/<id>',ImageAPIView.as_view()),
    
]
