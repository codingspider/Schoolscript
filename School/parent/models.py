from django.db import models


class Parent(models.Model):
    father_name = models.CharField(max_length=255, null=True, blank=True)
    father_occupation = models.CharField(max_length=255, null=True, blank=True)
    father_monthly_income = models.FloatField(max_length=255, null=True, blank=True)
    educational_qualification = models.CharField(max_length=255, null=True, blank=True)
    father_phone = models.IntegerField(null=True, blank=True)
    father_email = models.EmailField(max_length=255, blank=True, null=True)
    father_nid = models.IntegerField(null=True, blank=True)
    father_passport = models.CharField(max_length=255, null=True, blank=True)
    father_license = models.CharField(max_length=255, null=True, blank=True)
    mother_name = models.CharField(max_length=255, null=True, blank=True)
    mother_occupation = models.CharField(max_length=255, null=True, blank=True)
    mother_monthly_income = models.FloatField(max_length=255, null=True, blank=True)
    mother_educational_qualification = models.CharField(max_length=255, null=True, blank=True)
    mother_phone = models.IntegerField(null=True, blank=True)
    mother_email = models.EmailField(max_length=255, blank=True, null=True)
    mother_nid = models.IntegerField(null=True, blank=True)
    mother_passport = models.CharField(max_length=255, null=True, blank=True)
    mother_license = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.father_name

