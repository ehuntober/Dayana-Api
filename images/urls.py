
from django.urls import path   
# from django.views.generic import TemplateView
from .views import ImagesListView , HomepageView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'images' 
   
urlpatterns = [
    # path('',TemplateView.as_view(template_name="images/index.html")),
    path('',HomepageView.as_view(),name="Homepage"),
    path('images/',ImagesListView.as_view(),name='images'),
    
]

urlpatterns += staticfiles_urlpatterns()
 #url update
