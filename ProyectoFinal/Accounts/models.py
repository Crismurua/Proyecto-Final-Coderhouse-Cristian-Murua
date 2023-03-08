from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class UserExtra(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True, unique=True)
    location = models.CharField(max_length=50, null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.user.username

   
    
class Avatar(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatar/', null=True, blank=True, default='avatar/blank.png')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Avatars'