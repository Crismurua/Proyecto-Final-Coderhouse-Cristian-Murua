from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/', null=True, blank=True, default='default_product.png')
    description = models.TextField()
    price = models.FloatField()
    location = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    
class Comment(models.Model):
    comment = models.TextField(blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)  
    date = models.DateTimeField(auto_now_add=True)  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)