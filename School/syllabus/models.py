from django.db import models
from subject.models import Section, Class


class Syllabus(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(to='subject.Subject', on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True)
    note = models.TextField(null=True)

    def __str__(self):
        return self.title

