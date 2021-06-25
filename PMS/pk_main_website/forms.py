from django import forms
from django.forms import ModelForm

from .models import *

class Task_Form(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

class Board_Form(forms.ModelForm):

    class Meta:
        model = Board
        fields = '__all__'

class Category_Form(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        
        
