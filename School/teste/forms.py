from django import forms
from institute.models import Institute


class InstituteAddForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InstituteAddForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Institute
        fields = "__all__"



