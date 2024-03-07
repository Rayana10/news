from django import  forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm, UserCreationForm)
from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control','placeholder':'Введите имя пользователя'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-control', 'placeholder':'Введите пароль'
        })
    )
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrtionForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'введите имя'
    }))
   
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'введите фамилию'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'введите имя пользователя'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'введите email'
    }))
    
    password1= forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'введите пароль'
    }))
    password2= forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'подтвердите пароль'
    }))

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'введите имя'
    }))
   
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'введите фамилию'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'введите имя пользователя',
        'readonly':True
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'type':'email','placeholder':'введите email',
        'readonly':True
    }))
    
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control'
    }))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', )

    def save(self, commit=True):
        user = super(UserRegistrtionForm, self).save(commit=True)
        return user