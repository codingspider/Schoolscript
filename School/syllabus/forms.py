from django import forms
from django.forms import ModelForm
from .models import Syllabus


class SyllabusForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SyllabusForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Syllabus
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
