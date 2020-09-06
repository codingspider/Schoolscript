from django.db import models
from django.utils.timezone import now


class Attendance(models.Model):
    class_id = models.CharField(max_length=100, null=True, blank=True)
    section = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(default=now)
    student = models.CharField(max_length=100, null=True, blank=True)
    roll = models.CharField(max_length=100, null=True, blank=True)
    attendance = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateField(default=now)
    created_by = models.CharField(max_length=200, null=True, blank=True)



