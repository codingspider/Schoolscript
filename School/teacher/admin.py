from django.conf.urls import url
from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.html import format_html

from .models import Teacher


admin.site.register(Teacher)