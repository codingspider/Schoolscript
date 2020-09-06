from django.db import models
from geoposition.fields import GeopositionField
from django_google_maps import fields as map_fields


class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()


class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
