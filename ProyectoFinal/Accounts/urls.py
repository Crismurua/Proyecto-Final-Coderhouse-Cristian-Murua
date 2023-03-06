from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from Accounts.views import *

app_name = 'Accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='Project/logout.html'), name='logout'),
    path('user-edit/', user_edit, name='user-edit'),
    path('user-extra/', user_extra, name='user-extra'),
    path('avatar-edit/', upload_avatar, name='avatar-edit'),   
    
]