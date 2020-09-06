from django import forms

from .models import Student

GEEKS_CHOICES =(
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Other"),
)


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            self.fields['student_image'].widget.attrs['onchange'] = 'upload_img(this)'
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Student
        fields = '__all__'



