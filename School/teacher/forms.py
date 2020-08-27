from django import forms
from django_select2.forms import Select2Widget

from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'gender': Select2Widget,
            'staff_access': Select2Widget,

        }




