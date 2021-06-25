from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# create our custom user form that add more fields  
class CreateUserForm(UserCreationForm):
    # first_name = forms.CharField()
    # last_name = forms.CharField()

	class Meta:
		model = User
		fields = ['first_name',
				'last_name', 
				'username', 
				'email', 
				'password1', 
				'password2'
				]

