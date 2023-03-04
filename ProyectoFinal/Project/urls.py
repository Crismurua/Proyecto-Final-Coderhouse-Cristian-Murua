from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from Accounts.views import *

urlpatterns = [
    path('', home, name='home'),
    path('accounts/signup', signup, name='signup'),
    path('accounts/login', login_request, name='login'),
    path('accounts/logout', LogoutView.as_view(template_name='Project/logout.html'), name='logout'),
    path('accounts/user-edit', user_edit, name='user-edit'),
    path('accounts/avatar-edit', upload_avatar, name='avatar-edit'),
    path('products/', ProductList.as_view(), name='products'),
    path('product/<pk>', ProductDetail.as_view(), name='detail'),
    path('new-product/', NewProduct.as_view(), name='new-product'),
    path('update-product/<pk>', UpdateProduct.as_view(), name='update-product'),
    path('delete-product/<pk>', DeleteProduct.as_view(), name='delete-product'),
    
]