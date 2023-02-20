from django import forms

from AppBlog.models import Novedad

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroFormulario(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        
class LibroFormulario(forms.Form):
    titulo=forms.CharField()
    autorLib=forms.CharField(label='Autor del libro')
    autor=forms.CharField(label='Usuario')
    año=forms.IntegerField()
    puntaje=forms.IntegerField()
    reseña=forms.CharField()
    
class NovedadesFormulario(forms.ModelForm):

    class Meta:

        model = Novedad
        fields = ['titulo', 'año', 'imagen']
