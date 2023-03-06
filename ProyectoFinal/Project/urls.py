from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from Accounts.views import *

urlpatterns = [
    path('', ProductList.as_view(), name='home'),
    path('accounts/signup', signup, name='signup'),
    path('accounts/login', login_request, name='login'),
    path('accounts/logout', LogoutView.as_view(template_name='Project/logout.html'), name='logout'),
    path('accounts/user-edit', user_edit, name='user-edit'),
    path('accounts/user-extra', user_extra, name='user-extra'),
    path('accounts/avatar-edit', upload_avatar, name='avatar-edit'),
    path('my-products/', MyProductList.as_view(), name='my-products'),
    path('product/<pk>', ProductDetail.as_view(), name='detail'),
    path('product/<pk>', CommentList.as_view(), name='comment'),
    path('new-comment', NewComment.as_view(), name='new-comment'),
    path('new-product/', NewProduct.as_view(), name='new-product'),
    path('update-product/<pk>', UpdateProduct.as_view(), name='update-product'),
    path('delete-product/<pk>', DeleteProduct.as_view(), name='delete-product'),
    path('delete-comment/<pk>', DeleteComment.as_view(), name='delete-comment'),
    
    
]