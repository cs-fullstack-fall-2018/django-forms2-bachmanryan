from django import forms
from .models import FormModel


class ModelForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = {'name'}
