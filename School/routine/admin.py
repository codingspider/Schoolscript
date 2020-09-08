from django.contrib import admin
from .models import *
from . import models


class TimeTableItemInline(admin.TabularInline):
    model = models.TimeTableItem
    raw_id_fields = ['subject']
    extra = 1


@admin.register(models.TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['course', 'day']
    inlines = [TimeTableItemInline]
