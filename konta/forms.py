from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from konta.models import Profil


class UzytkownikForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfilForm(forms.ModelForm):
    class Meta():
        model = Profil
        fields = ('imie', 'nazwisko', 'klasa', 'zdjecie')
