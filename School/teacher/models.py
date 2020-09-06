from django.contrib.auth.models import User
from django.db import models

G_CHOICES =(
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Other"),
)

Access_CHOICES = (
    ("1", "Teacher"),
    ("2", "Staff"),
)


class Teacher(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='teacher')
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=2, choices=G_CHOICES)
    teacher_designation = models.CharField(max_length=255, null=True, blank=True)
    work_type = models.CharField(max_length=255, null=True, blank=True)
    monthly_salary = models.FloatField(null=True, blank=True)
    special_for = models.CharField(max_length=255, null=True, blank=True)
    educational_qualification = models.CharField(max_length=255, null=True, blank=True)
    special_training = models.CharField(max_length=255, null=True, blank=True)
    joining_date = models.DateField(null=True,blank=True)
    retirement_date = models.DateField(null=True, blank=True)
    index_number = models.IntegerField(null=True, blank=True)
    mpo_date = models.DateField(null=True, blank=True)
    staff_id_no = models.IntegerField(null=True, blank=True)
    staff_access = models.CharField(max_length=2, null=True, blank=True, choices=Access_CHOICES)
    teacher_email = models.EmailField(max_length=255, null=True)
    teacher_password = models.CharField(max_length=255, null=True,)
    teacher_phone = models.IntegerField(null=True, blank=True)
    teacher_dob = models.DateField(null=True)
    blood_group = models.CharField(max_length=20, null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    passport = models.CharField(max_length=100, null=True, blank=True)
    nid = models.IntegerField(null=True)
    last_organizing = models.CharField(max_length=255, null=True, blank=True)
    cause_of_leave = models.CharField(max_length=255, null=True, blank=True)
    institute_address = models.CharField(max_length=255, null=True, blank=True)
    village = models.CharField(max_length=255, blank=True, null=True)
    post = models.CharField(max_length=255, blank=True, null=True)
    union = models.CharField(max_length=255, blank=True, null=True)
    upozilla = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    permanent_village = models.CharField(max_length=255, blank=True, null=True)
    permanent_post = models.CharField(max_length=255, blank=True, null=True)
    permanent_union = models.CharField(max_length=255, blank=True, null=True)
    permanent_upozilla = models.CharField(max_length=255, blank=True, null=True)
    permanent_district = models.CharField(max_length=255, blank=True, null=True)
    permanent_postal_code = models.IntegerField( blank=True, null=True)

    image = models.ImageField(null=True, blank=True, upload_to='uploads/')

    def __str__(self):
        return self.first_name



