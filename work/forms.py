from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *
from tkinter import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = details
        fields = '__all__'