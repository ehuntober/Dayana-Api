from django.db import models

# Create your models here.
from django.utils import timezone 
from django.contrib.auth.models import User 

def user_directory_path(instance,filename):
    # remove any trailing slashes from the filename
    filename = filename.rstrip('/')
    # return the desired path for the uploaded image
    return f"images/{filename}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Images(models.Model):
    
    options = (
        ('active', 'Active'),
        ('deactivated','Deactivated')
    )
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    alt = models.TextField(null=True)
    image = models.ImageField(
        upload_to=user_directory_path, default='posts/default.jpg')
    slug =models.SlugField(max_length=250, unique_for_date='created')
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT,related_name='author')
    status = models.CharField(max_length=11,choices=options,default = 'active')

