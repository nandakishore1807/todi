from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = details
        fields = '__all__'