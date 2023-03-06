from django.urls import path
from .views import *

app_name = 'Project'

urlpatterns = [
    path('', ProductList.as_view(), name='home'),
    path('my-products/', MyProductList.as_view(), name='my-products'),
    path('product/<pk>', ProductDetail.as_view(), name='detail'),
    path('like/', like, name='like'),
    path('comment/', comment, name='comment'),
    #path('product/<pk>', CommentList.as_view(), name='comment'),
    #path('new-comment', NewComment.as_view(), name='new-comment'),
    path('new-product/', NewProduct.as_view(), name='new-product'),
    path('update-product/<pk>', UpdateProduct.as_view(), name='update-product'),
    path('delete-product/<pk>', DeleteProduct.as_view(), name='delete-product'),
    path('delete-comment/<pk>', DeleteComment.as_view(), name='delete-comment'),
    
    
]