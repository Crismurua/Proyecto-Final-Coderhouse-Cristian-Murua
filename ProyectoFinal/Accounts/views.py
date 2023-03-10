from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.views.generic.detail import DetailView

from .forms import MyUserCreationForm, UserEditForm, AvatarForm, UserExtraCreate, UserEditExtraForm

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
                return redirect('project:home')
            else:
                context = {'message': f'User not found!', 'form': form}
                return render(request, 'login.html', context)
        else:
            context = {'message': f'Incorrect data!', 'form': form}
            return render(request, 'login.html', context)
    
    context = {'form': form}
    return render(request, 'login.html', context)


def signup(request):
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, request.FILES)
        form2 = UserExtraCreate(request.POST, request.FILES)
        avatar_form = AvatarForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid() and avatar_form.is_valid():
            user = form.save()
            form2.instance.user = user
            avatar_form.instance.user = user
            form2.save()
            avatar_form.save()
            # group = Group.objects.get(name='user-extra')
            # user.groups.add(group)
            
            return redirect('accounts:login')
    else:      
        form = MyUserCreationForm()
        form2 = UserExtraCreate()
        avatar_form = AvatarForm()
    context = {'form': form, 'form2': form2, 'avatar_form': avatar_form}
    return render(request, 'signup.html', context)
    
    
@login_required
def user_edit(request):
    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data            
            
            user.username = info['username']
            user.email = info['email']
            user.first_name = info['first_name']
            user.last_name = info['last_name']

            user.save()
            

            return redirect('project:home')
    
    else:
        form = UserEditForm(initial={
                                    'username': user.username,
                                    'email': user.email,
                                    'last_name': user.last_name,
                                    'first_name': user.first_name,
                                    })

    return render(request, 'user-edit.html', {'form': form})

@login_required
def user_extra(request):
    user = request.user.userextra
    form = UserEditExtraForm(instance=user)

    if request.method == 'POST':
        form = UserEditExtraForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            

            return redirect('project:home')
    
    else:
        form = UserEditExtraForm(initial={
                                    'phone': user.phone,
                                    'location': user.location,
                                    })

    return render(request, 'user-extra.html', {'form': form})


@login_required
def upload_avatar(request):
    avatar = request.user.avatar
    avatar_form = AvatarForm(instance=avatar)

    if request.method == 'POST':
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if avatar_form.is_valid():
            avatar_form.save()

            return redirect('project:home')

    else:
        return render(request, 'avatar-edit.html', {'avatar_form': avatar_form})


class UserDetail(DetailView):
    
    model = User
    template_name = 'user-detail.html'
