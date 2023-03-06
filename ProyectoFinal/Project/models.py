from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/', null=True, blank=True, default='products/default_product.png')
    description = models.TextField()
    price = models.FloatField()
    location = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])
    
    @property
    def get_comments(self):
        own_comments = Comment.objects.filter(product=self)
        return own_comments
    
    
class Comment(models.Model):
    comment = models.TextField(blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='user_like')
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='comments')  
    date = models.DateTimeField(auto_now_add=True)  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user} --> {self.comment}'