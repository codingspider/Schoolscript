from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django import forms
from django.forms import SelectDateWidget, Field, fields
from django.utils.safestring import mark_safe
from institute.models import Institute, City, State
from .choices import *


#     # TIME_FORMAT = '%I:%M %p'
#     # date = forms.CharField(
#     #     widget=TimePickerInput(format='%I:%M %p')
#     # )
#
# date = forms.CharField(
#     widget=DatePickerInput(format='%m/%d/%Y')
# )


class ImagePreviewWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super().render(name, value, attrs=None, **kwargs)
        img_html = mark_safe(f'<br><br><img src="{value.url}"/>')
        return f'{input_html}{img_html}'


class AddInstituteForm(forms.ModelForm):

    agree = forms.BooleanField(initial=True, required=True)

    def __init__(self, *args, **kwargs):
        super(AddInstituteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['institute_logo'].widget.attrs.update({'class': ''})
            self.fields['principle_signature'].widget.attrs.update({'class': ''})
            self.fields['institute_logo'].widget.attrs['onchange'] = 'upload_img(this)'
            self.fields['principle_signature'].widget.attrs['onchange'] = 'prin_sig(this)'

    class Meta:
        model = Institute
        fields = "__all__"
        exclude = ('agree',)
        institute_logo = forms.ImageField(widget=ImagePreviewWidget, )
        widgets = {

            'established_date': DatePickerInput(format='%Y-%m-%d'),  # specify date-frmat
        }


class InstituteImageUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InstituteImageUpdate, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            self.fields['institute_logo'].widget.attrs['onchange'] = 'upload_img(this)'
            self.fields['principle_signature'].widget.attrs['onchange'] = 'prin_sig(this)'

    class Meta:
        model = Institute
        fields = "institute_logo", "principle_signature"









