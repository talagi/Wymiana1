from django import forms
from wymiana.models import Komentarz, WymianaPlik


class KomentarzForm(forms.ModelForm):
    class Meta:
        model = Komentarz
        fields = ['tresc']


class PlikForm(forms.ModelForm):
    class Meta:
        model = WymianaPlik
        fields = ['plik', ]
        widgets = {
            'plik': forms.ClearableFileInput(attrs={'multiple': True}),
        }
