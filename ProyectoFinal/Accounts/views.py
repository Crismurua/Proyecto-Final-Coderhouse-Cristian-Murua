from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

from .forms import MyUserCreationForm, UserEditForm, AvatarForm, UserEdit2

# Create your views here.
def login_request(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=user, password=password)

            if user is not None:
                login(request, user)
                context = {'message': f'Welcome {user}'}
                return render(request, 'Project/home.html', context)
            else:
                context = {'message': f'User not found!', 'form': form}
                return render(request, 'Project/login.html', context)
        else:
            context = {'message': f'Incorrect data!', 'form': form}
            return render(request, 'Project/login.html', context)
    
    context = {'form': form}
    return render(request, 'Project/login.html', context)


def signup(request):
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['username']
            context = {'menssage': 'User successfully created!'}
            return render(request, 'Project/home.html', context)
    else:      
        form = MyUserCreationForm()
        context = {'form': form}
        return render(request, 'Project/signup.html', context)
    
    
@login_required
def user_edit(request):
    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        form2 = UserEdit2(request.POST)
        form2.instance.user = form
        if form.is_valid() and form2.is_valid():
            info = form.cleaned_data
            info2 = form2.cleaned_data
            
            
            user.username = info['username']
            user.email = info['email']
            user.first_name = info['first_name']
            user.last_name = info['last_name']
            
            user.phone = info2['phone']
            user.location = info2['location']
            
            group = Group.objects.get(name='user-edit')
            user.groups.add(group)

            user.save()
            

            return redirect('/')
    
    else:
        form = UserEditForm(initial={
                                    'username': user.username,
                                    'email': user.email,
                                    'last_name': user.last_name,
                                    'first_name': user.first_name,
                                    })
        
        form2 = UserEdit2(initial={
                                    'phone': user.phone,
                                    'location': user.location,
                                    })

    return render(request, 'Project/user-edit.html', {'form': form, 'form2': form2})


@login_required
def upload_avatar(request):
    avatar = request.user.avatar
    avatar_form = AvatarForm(instance=avatar)

    if request.method == 'POST':
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if avatar_form.is_valid():
            avatar_form.save()

            return redirect('/')

    else:
        return render(request, 'Project/avatar-edit.html', {'avatar_form': avatar_form})
