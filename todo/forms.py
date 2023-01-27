from .models import Todo
from django import forms


class ToDoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ('status',)
