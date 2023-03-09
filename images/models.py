from django.db import models

# Create your models here.
from django.utils import timezone 
from django.contrib.auth.models import User 

def user_directory_path(instance,filename):
    return 'images/{0}/'.format(filename)

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Images(models.Model):
    
