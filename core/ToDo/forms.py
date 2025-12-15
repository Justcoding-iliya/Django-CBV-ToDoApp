from django import forms
from .models import Task

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'complate'] 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'complate': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
