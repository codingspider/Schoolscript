from django.db import models

# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('x', 'Other'),
    )


class Student(models.Model):
    institute_name = models.CharField(max_length=255, null=True, )
    student_name = models.CharField(max_length=255, null=True, )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)
    student_class = models.CharField(max_length=20, null=True,)
    shift = models.CharField(max_length=50, null=True)
    section = models.CharField(max_length=50, null=True)
    group= models.CharField(max_length=255, null=True)
    id_number = models.IntegerField(blank=True, null=True)
    class_roll = models.IntegerField(blank=True, null=True)
    session = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(max_length=100, blank=True, null=True)
    blood_group = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)
    birth_id_number = models.IntegerField(null=True)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)
    old_school_address = models.CharField(max_length=255, null=True, blank=True)
    cause_for_leave = models.CharField(max_length=255, null=True, blank=True)
    house_no = models.CharField(max_length=255, blank=True, null=True)
    house_name = models.CharField(max_length=255, blank=True, null=True)
    road_no = models.CharField(max_length=255, blank=True, null=True)
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
    permanent_postal_code = models.IntegerField(blank=True, null=True)
    student_image = models.ImageField(null=True, blank=True, upload_to='uploads/')



