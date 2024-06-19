from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm): # NOT WORKING FORM
    class Meta:
        model = CustomUser
        fields = ('username', 'email',) 