from django import forms
from .models import Federal


class FederalForm(forms.ModelForm):
    class Meta:
        model = Federal
        fields = ['email', 'password']