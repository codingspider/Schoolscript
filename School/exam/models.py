from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render
from django.utils.timezone import now
from subject.models import Subject, Class, Section


class ExamType(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Exam(models.Model):
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE, null=True)
    exaam_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    exam_date = models.DateField(default=now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.IntegerField()
    description = models.TextField(null=True, blank=True)


class Result(models.Model):
    class_id = models.CharField(max_length=100, blank=True, null=True)
    subject_id = models.CharField(max_length=100, blank=True, )
    subject_type = models.CharField(max_length=100, blank=True, )
    exam_type = models.CharField(max_length=100, blank=True, )
    student_roll = models.CharField(max_length=100, blank=True, )
    pass_mark = models.CharField(max_length=100, blank=True, )
    written_mark = models.CharField(max_length=100, blank=True, null=True)
    mcq_mark = models.CharField(max_length=100, blank=True, )
    practical_mark = models.CharField(max_length=100, blank=True, )
    viva_mark = models.CharField(max_length=100, blank=True, )
    created_at = models.DateField(default=now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True, blank=True)




