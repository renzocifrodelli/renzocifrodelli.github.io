from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class NewsForm(forms.Form):
    tittle = forms.CharField(max_length=40)
    subtittle = forms.CharField(max_length=40)
    notice = forms.CharField(max_length=4000)
    
class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)