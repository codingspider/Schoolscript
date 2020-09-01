from django.db import models
from .choicestatus import gender_status,blood_group,choice_status,religion_status, work_type
from hostels.models import Designation


class Group(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Professionals(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=5, choices=gender_status)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    work_type = models.CharField(max_length=5, choices=work_type)
    monthly_salary = models.FloatField(null=True, blank=True)
    special_for = models.CharField(max_length=255, null=True, blank=True)
    educational_qualification = models.CharField(max_length=255, null=True, blank=True)
    special_training = models.CharField(max_length=255, null=True, blank=True)
    joining_date = models.CharField(max_length=255, null=True, blank=True)
    retirement_date = models.CharField(max_length=200, null=True, blank=True)
    index_number = models.IntegerField(null=True, blank=True)
    mpo_date = models.CharField(max_length=200, null=True, blank=True)
    staff_id_no = models.IntegerField(null=True, blank=True)
    staff_access = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher_email = models.EmailField(max_length=255, null=True)
    teacher_password = models.CharField(max_length=255, null=True,)
    teacher_phone = models.IntegerField(null=True, blank=True)
    birth_date = models.CharField(max_length=255, null=True)
    blood_group = models.CharField(max_length=5, choices=blood_group)
    religion = models.CharField(max_length=5, choices=religion_status)
    passport = models.CharField(max_length=100, null=True, blank=True)
    nid = models.CharField(max_length=255, null=True, blank=True)
    last_organizing = models.CharField(max_length=255, null=True, blank=True)
    cause_of_leave = models.CharField(max_length=255, null=True, blank=True)
    institute_address = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=5, choices=choice_status)

    house_number = models.CharField(max_length=100, null=True, blank=True)
    road_number = models.CharField(max_length=100, null=True, blank=True)
    village = models.CharField(max_length=100, null=True, blank=True)
    post_office = models.CharField(max_length=100, null=True, blank=True)
    union_name = models.CharField(max_length=100, null=True, blank=True)
    thana = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    post_code = models.CharField(max_length=100, null=True, blank=True)
    is_permanent = models.BooleanField(default=True, null=True, blank=True)

    per_house_number = models.CharField(max_length=100, null=True, blank=True)
    per_road_number = models.CharField(max_length=100, null=True, blank=True)
    per_village = models.CharField(max_length=100, null=True, blank=True)
    per_post_office = models.CharField(max_length=100, null=True, blank=True)
    per_union_name = models.CharField(max_length=100, null=True, blank=True)
    per_thana = models.CharField(max_length=100, null=True, blank=True)
    per_district = models.CharField(max_length=100, null=True, blank=True)
    per_post_code = models.CharField(max_length=100, null=True, blank=True)

    image = models.ImageField(null=True, blank=True, upload_to='staff/')

    def __str__(self):
        return self.first_name


class FamilyInformation(models.Model):
    staff = models.IntegerField(null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    father_occupation = models.CharField(max_length=255, null=True, blank=True)
    father_monthly_income = models.FloatField(max_length=255, null=True, blank=True)
    father_qualification = models.CharField(max_length=255, null=True, blank=True)
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
    nid = models.IntegerField(max_length=255, null=True, blank=True)
    spouse_name = models.CharField(max_length=255, null=True, blank=True)
    spouse_occupation = models.CharField(max_length=255, null=True, blank=True)
    marrige_day = models.DateField(null=True, blank=True)
    spouse_education = models.CharField(max_length=255, null=True, blank=True)
    kids = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.father_phone

