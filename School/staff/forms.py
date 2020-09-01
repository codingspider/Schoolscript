from bootstrap_datepicker_plus import YearPickerInput, DatePickerInput
from django import forms
from django_select2.forms import Select2Widget

from .models import Professionals, FamilyInformation


class ProfessionalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfessionalForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Professionals
        fields = '__all__'
        widgets = {

            'birth_date': DatePickerInput(format='%d-%m-%Y'),
            'marrige_day': DatePickerInput(format='%d-%m-%Y'),
            'joining_date': DatePickerInput(format='%d-%m-%Y'),
            'retirement_date': DatePickerInput(format='%d-%m-%Y'),
            'mpo_date': DatePickerInput(format='%d-%m-%Y'),

        }


class ProfessionalEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfessionalEditForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Professionals
        fields = '__all__'
        exclude = ('teacher_email','teacher_password')
        widgets = {

            'birth_date': DatePickerInput(format='%d-%m-%Y'),
            'marrige_day': DatePickerInput(format='%d-%m-%Y'),
            'joining_date': DatePickerInput(format='%d-%m-%Y'),
            'retirement_date': DatePickerInput(format='%d-%m-%Y'),
            'mpo_date': DatePickerInput(format='%d-%m-%Y'),

        }



class FamilyInformationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FamilyInformationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = FamilyInformation
        fields = '__all__'
        widgets = {

            'birth_date': DatePickerInput(format='%d-%m-%Y'),
            'marrige_day': DatePickerInput(format='%d-%m-%Y'),
            'joining_date': DatePickerInput(format='%d-%m-%Y'),
            'retirement_date': DatePickerInput(format='%d-%m-%Y'),
            'mpo_date': DatePickerInput(format='%d-%m-%Y'),

        }
