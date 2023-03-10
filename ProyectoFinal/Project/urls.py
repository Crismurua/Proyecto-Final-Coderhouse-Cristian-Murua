from django.urls import path
from .views import *

app_name = 'Project'

urlpatterns = [
    path('', ProductList.as_view(), name='home'),
    path('about/', about, name='about'),
    path('not-found/', notfound, name='not-found'),
    path('my-products/', MyProductList.as_view(), name='my-products'),
    path('product/<pk>', ProductDetail.as_view(), name='detail'),
    path('like/', like, name='like'),
    path('comment/', comment, name='comment'),
    path('comment-list/', CommentList.as_view(), name='comment-list'),
    path('new-product/', NewProduct.as_view(), name='new-product'),
    path('update-product/<pk>', UpdateProduct.as_view(), name='update-product'),
    path('delete-product/<pk>', DeleteProduct.as_view(), name='delete-product'),
    path('delete-comment/<pk>', DeleteComment.as_view(), name='delete-comment'),
    path('search/', search, name='search'),
    
    
]