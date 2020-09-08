from django import forms

from .models import TimeTable, TimeTableItem


class TimeTableItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TimeTableItemForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = TimeTableItem
        fields = '__all__'
