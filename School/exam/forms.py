from django import forms
from django.forms import ModelForm
from .models import *


class ExamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model= Exam
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }


class ExamTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExamTypeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model= ExamType
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }


class ResultForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExamTypeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model= ExamType
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }


class GradeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GradeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model= Grade
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }
