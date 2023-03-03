from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar, UserEdit

class MyUserCreationForm(UserCreationForm):

    username = forms.CharField(label='Username', widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}
        

class UserEditForm(forms.Form):

    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:

        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {k: '' for k in fields}
        
class UserEdit2(forms.Form):
    
    phone = forms.IntegerField(label='Phone Number')
    location = forms.CharField(label='Location')
    
    class Meta:

        model = UserEdit
        fields = ['phone', 'location']
        help_texts = {k: '' for k in fields}
        
        
class AvatarForm(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = '__all__'
        exclude = ['user']