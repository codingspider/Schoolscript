from django.db import models
from django.utils import timezone

from .choices import *


class Country(models.Model):
    iso = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    nicename = models.CharField(max_length=255, null=True)
    iso3 = models.CharField(max_length=255, null=True, )
    numcode = models.IntegerField(null=True, )
    phonecode = models.IntegerField(null=True, )

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    bn_name = models.CharField(max_length=255, null=True)
    lat = models.CharField(max_length=100, null=True)
    lon =models.CharField(max_length=100, null=True)
    url =models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, blank=False, on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    bn_name =models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)


def __str__(self):
        return self.city


class Institute(models.Model):
    name = models.CharField(max_length=255)
    email_1 = models.EmailField(max_length=100,)
    email_2 = models.EmailField(max_length=100, null=True,)
    website = models.URLField(max_length=100)
    institute_code = models.CharField(max_length=100, )
    address_1 = models.CharField(max_length=500)
    address_2 = models.CharField(max_length=500,null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    zip = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    established_date = models.CharField(max_length=255, null=True, blank=True)
    phone_1 = models.CharField(max_length=15)
    phone_2 = models.CharField(max_length=15,null=True, blank=True)
    fax = models.CharField(max_length=15,null=True, blank=True)
    active_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=1)
    agree = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    institute_logo = models.ImageField(null=True, blank=True, max_length=255, upload_to='' )
    principle_signature = models.ImageField(max_length=255, null=True, blank=True, upload_to='')

    def __str__(self):
        return self.name

    # class Meta:
    #     db_table = 'institute'


class ImageUpload(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/')


class StatusChoice(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True)


class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return self.month


