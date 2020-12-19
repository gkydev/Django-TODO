from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ["name", "description", "completed"]

class ListForm(forms.ModelForm):

    class Meta:
        model = ToDoList
        fields = ["name"]