from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username',
        'class': INPUT_CLASSES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': INPUT_CLASSES
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Choose a username',
        'class': INPUT_CLASSES
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email address',
        'class': INPUT_CLASSES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Create a password',
        'class': INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm your password',
        'class': INPUT_CLASSES
    }))