from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Ingresa Nombre",'autofocus': ''}))
    last_name = forms.CharField(label="Apellido", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Ingresa Apellidos",'autofocus': ''}))
    username = forms.CharField(label="Usuario", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Ingresa usuario",'autofocus': ''}))
    email = forms.EmailField(label="Dirección de Correo Electrónico", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Dirección de Correo Electrónico",'autofocus': ''}))
    password1 = forms.CharField(label="Contraseña", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder': "Ingresa contraseña"}))
    password2 = forms.CharField(label="Confirmar contraseña", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Confirmar contraseña"}))
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        help_text = {k: "" for k in fields} #remover los textos de ayuda 
    

