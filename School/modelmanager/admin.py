from django.contrib import admin

# Register your models here.
from .models import Document


class DocumentModel(admin.ModelAdmin):
    list_display = ('id','name', 'size', 'file_type')


admin.site.register(Document, DocumentModel)