from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Product, Comment
from .forms import ProductForm, CommentForm

# Create your views here.
def home(request):
    return render(request, 'Project/home.html')

class ProductList(ListView):
    
    model = Product
    template_name = 'Project/product-list.html'
    
class ProductDetail(DetailView):
    
    model = Product
    template_name = 'Project/product-detail.html'
    
class NewProduct(LoginRequiredMixin, CreateView):

    model = Product
    template_name = 'Project/new-product.html'
    success_url = reverse_lazy('home')
    fields = ['name', 'image', 'description', 'price', 'location', 'available']
    
class UpdateProduct(LoginRequiredMixin, UpdateView):

    login_url = 'login/'
    model = Product
    template_name = 'Project/new-product.html'
    success_url = reverse_lazy('home')
    fields = ['name', 'image', 'description', 'price', 'location', 'available']
    
class DeleteProduct(LoginRequiredMixin, DeleteView):

    model = Product
    template_name = 'Project/delete-product.html'
    success_url = reverse_lazy('home')
    
class CommentList(ListView):
    
    model = Comment
    template_name = 'Project/comment-list.html'
    
class NewComment(LoginRequiredMixin, CreateView):

    model = Comment
    template_name = 'Project/new-comment.html'
    success_url = reverse_lazy('home')
    fields = ['comment']
    
class DeleteComment(LoginRequiredMixin, DeleteView):

    model = Comment
    template_name = 'Project/delete-comment.html'
    success_url = reverse_lazy('home')