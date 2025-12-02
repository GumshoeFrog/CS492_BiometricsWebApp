from django import forms
from .models import Restaurant

# Creates a form that make use of the Restaurant database model
class RestaurantForm(forms.ModelForm):
    class Meta:
        # take information from Restaurant database
        model = Restaurant
        # request the email and password fields
        fields = ['email', 'password']