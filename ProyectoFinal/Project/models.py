from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products', null=True, blank=True, default='default_product.png')
    description = models.TextField()
    price = models.FloatField()
    location = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    
class Comment(models.Model):
    comment = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    date = models.DateField(auto_now=True)  