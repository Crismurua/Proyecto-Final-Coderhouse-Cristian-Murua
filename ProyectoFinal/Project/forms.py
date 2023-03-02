from django import forms

class ProductForm(forms.Form):
    name = forms.CharField()
    image = forms.ImageField()
    description = forms.CharField(label='Description', widget=forms.TextInput)
    price = forms.FloatField()
    location = forms.CharField()
    available = forms.BooleanField()
    
class CommentForm(forms.Form):
    comment = forms.CharField(label='Comment', widget=forms.TextInput)
    