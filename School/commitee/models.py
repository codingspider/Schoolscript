from django.db import models


G_CHOICES =(
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Other"),
)

COMMITTEE = (
    ("1", "সভাপতি"),
    ("1", "অধ্যক্ষ/সচিব"),
    ("1", "সম্পাদক"),
    ("1", "বিদ্যুৎসাহী"),
    ("1", "দাতা সদস্য"),
    ("1", "অভিভাবক সদস্য"),
    ("1", "শিক্ষক প্রতিনিধি"),
)

class Commitee(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=2, choices=G_CHOICES)
    educational_qualification = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=2, choices=COMMITTEE)
    joining_date = models.DateField(null=True, blank=True)
    expire_date = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    nid = models.IntegerField(null=True, blank=True)
    passport = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True, )
    village = models.CharField(max_length=255, blank=True, null=True)
    post = models.CharField(max_length=255, blank=True, null=True)
    union = models.CharField(max_length=255, blank=True, null=True)
    upozilla = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')

    def __str__(self):
        return self.full_name