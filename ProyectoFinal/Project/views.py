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
    template_name = 'Project/home.html'
    
class MyProductList(LoginRequiredMixin, ListView):
    
    model = User
    template_name = 'Project/product-list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
    
class ProductDetail(DetailView):
    
    model = Product
    template_name = 'Project/product-detail.html'
    
class NewProduct(LoginRequiredMixin, CreateView):

    model = Product
    template_name = 'Project/new-product.html'
    success_url = reverse_lazy('my-products')
    form_class = ProductForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(NewProduct, self).form_valid(form)
    
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
    
class CommentList(LoginRequiredMixin, ListView):
    
    model = Product
    template_name = 'Project/product-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
       
        
    
class NewComment(LoginRequiredMixin, CreateView):

    model = Comment
    template_name = 'Project/new-comment.html'
    success_url = reverse_lazy('home')
    form_class = CommentForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = self.request.product
        form.save()
        return super(NewComment, self).form_valid(form)
    
class DeleteComment(LoginRequiredMixin, DeleteView):

    model = Comment
    template_name = 'Project/delete-comment.html'
    success_url = reverse_lazy('home')