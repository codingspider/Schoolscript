import os

from django.core.exceptions import ValidationError
from django.db import models
from subject.models import Section, Class


def validate_file(file):
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.ppt', '.pptx', '.text']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please choose these  %s file type' % valid_extensions)
    file_size = file.file.size
    limit_mb = 250
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_mb)


class Syllabus(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(to='subject.Subject', on_delete=models.CASCADE)
    file = models.FileField(upload_to='ebook', null=True, blank=True, validators=[validate_file])
    note = models.TextField(null=True)

    def __str__(self):
        return self.title

