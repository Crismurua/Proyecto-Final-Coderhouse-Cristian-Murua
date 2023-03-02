from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from Accounts.views import *

urlpatterns = [
    path('', home, name='home'),
    path('accounts/signup', signup, name='signup'),
    path('accounts/login', login_request, name='login'),
    path('accounts/logout', LogoutView.as_view(template_name='Project/logout.html'), name='logout'),
    path('accounts/user-edit', user_edit, upload_avatar, name='user-edit'),
]