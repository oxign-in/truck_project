from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.forms import ModelForm
from apps.materials.models import Materials


# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class MaterialsForm(ModelForm):
	class Meta:
		model = Materials
		fields = ['name', 'delivery_date', 'weight', 'source', 'destination']