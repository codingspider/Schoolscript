from django import forms
from django.forms import ModelForm
from .models import *


class SubjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Subject
        fields ='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }


class GroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Group
        fields ='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }


class SubjectTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubjectTypeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = SubjectType
        fields ='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }


class ClassForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Class
        fields ='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }


class SectionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Section
        fields ='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }


