from django.contrib import admin

# Register your models here.

from .models import *


class CountryModel(admin.ModelAdmin):
    list_display = ('name',)


class CityModel(admin.ModelAdmin):
    list_display = ('name',)


class StateModel(admin.ModelAdmin):
    list_display = ('name', 'id',)
    search_fields = ('name',)


admin.site.register(Institute)
admin.site.register(ImageUpload)
# admin.site.register(Country, CountryModel)
# admin.site.register(City, CityModel)
# admin.site.register(State, StateModel)