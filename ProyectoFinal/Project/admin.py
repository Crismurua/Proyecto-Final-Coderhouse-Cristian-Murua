from django.contrib import admin
from .models import *
from Accounts.models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Avatar)
admin.site.register(UserExtra)
