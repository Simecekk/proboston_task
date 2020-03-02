from django import forms
from .models import FormModel

class FormModelForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = ['jméno', 'email', 'ičo']
        widgets = {
            'jméno': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'ičo': forms.TextInput(attrs={'class': 'form-control'})
        }