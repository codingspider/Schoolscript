from django import forms
from django.forms import ModelForm
from .models import *


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields ='__all__'
