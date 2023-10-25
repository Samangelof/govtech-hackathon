from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from schools.models import Students

class RegisterStudentForm(forms.ModelForm):
    username = forms.CharField(label='Введите имя:', 
        widget=forms.TextInput(attrs={'class': 'inp', 'placeholder': "Почта"}))

    surname = forms.CharField(label='Введите фамилию:', 
        widget=forms.TextInput(attrs={'class': 'inp', 'placeholder': "Фамилия"}))

    email = forms.EmailField(label='Введите почту', 
        widget=forms.EmailInput(attrs={'class': 'inp', 'placeholder': "Почта"}))

    student_school = forms.CharField(label='Введите школу', 
        widget=forms.TextInput(attrs={'class': 'inp', 'placeholder': "Школа №1"}))

    student_class = forms.CharField(label='Введите класс', 
        widget=forms.TextInput(attrs={'class': 'inp', 'type': 'number', 'placeholder': "1-11"}))

    individual_number = forms.CharField(label='Введите ИИН', 
        widget=forms.TextInput(attrs={'class': 'inp', 'placeholder': "ИИН"}))

    phone = forms.CharField(label='Введите номер телефона', 
        widget=forms.TextInput(attrs={'class': 'inp', 'value':"+7(___)___-__-__"}))


    image_file = forms.FileField(label='Прикрепить фото', 
        widget=forms.FileInput(attrs={'class': 'inp', 'type':'file'}))
        
    password1 = forms.CharField(label='Введите пароль', 
        widget=forms.TextInput(attrs={'class': 'inp', 'type': 'password'}))

    class Meta:
        model = Students
        fields = ('username', 'surname', 'email', 'student_school', 'student_class','individual_number', 'phone', 'image_file', 'password1')
        # fields = ('username', 'surname', 'email')


class AuthUserForm(forms.ModelForm):
    username = forms.CharField(label='Введите почту', 
        widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': "Почта"}
    ))
    password = forms.CharField(label='Введите пароль', 
        widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'type': 'password', 'placeholder': "Пароль"}
    ))

    class Meta:
        model = Students
        fields = ('username', 'password', )