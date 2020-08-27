from django import forms
from django_select2.forms import Select2Widget

from .models import Commitee


class CommitteeForm(forms.ModelForm):
    class Meta:
        model = Commitee
        fields = '__all__'
        widgets = {
            'gender': Select2Widget,
            'staff_access': Select2Widget,

        }




