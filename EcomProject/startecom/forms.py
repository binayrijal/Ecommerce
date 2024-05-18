from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    
    username=forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Input your username',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))



class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password','password2']
        
    username=forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Input your username',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder': 'Input your email',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Re-password here',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))