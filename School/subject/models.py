from django.db import models
from teacher.models import Teacher


class Section(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class SubjectType(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    subject_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    type = models.ForeignKey(SubjectType, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=10, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    pass_mark = models.IntegerField(null=True, blank=True)
    total_mark = models.IntegerField(null=True, blank=True)
    viva_mark = models.IntegerField(null=True, blank=True)
    written_mark = models.IntegerField(null=True, blank=True)
    msq_mark = models.IntegerField(null=True, blank=True)
    practical_mark = models.IntegerField(null=True, blank=True)
    credit = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name




