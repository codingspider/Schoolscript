from django.db import models
from django.utils.timezone import now

from .choices import day
from teacher.models import Teacher
from subject.models import Subject, Class


class TimeTable(models.Model):
    DAYS_OF_THE_WEEK = (
        ('1', 'Saturday'),
        ('2', 'Sunday'),
        ('3', 'Monday'),
        ('4', 'Tuesday'),
        ('5', 'Wednesday'),
        ('6', 'Thursday'),
        ('7', 'Friday')
    )
    course = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    day = models.CharField(max_length=2, choices=DAYS_OF_THE_WEEK, null=True, blank=True)
    created_at = models.DateField(default=now)

    class Meta:
        verbose_name = 'timetable'
        verbose_name_plural = 'timetables'


class TimeTableItem(models.Model):
    time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    start_time = models.TimeField(default=now)
    end_time = models.TimeField(default=now)
    created_at = models.DateField(default=now)

    class Meta:
        ordering = ('start_time',)

