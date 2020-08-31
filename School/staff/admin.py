from django.contrib import admin

# Register your models here.
from .models import Professionals, Group, FamilyInformation

admin.site.register(Professionals)
admin.site.register(Group)
admin.site.register(FamilyInformation)