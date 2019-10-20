#forms.py

from django import forms

from django.contrib.auth.models import User
from ounjeapp.models import Merchant

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required =True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = {"username", "password", "first_name", "last_name", "email"}

class MerchantForm(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = {"name", "phone", "address", "logo"}
