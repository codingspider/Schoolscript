from django.contrib import admin
from .models import ExamType, Exam, Result
# Register your models here.


class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam_type', 'exam_date', 'start_time', 'end_time')


class ResultAdmin(admin.ModelAdmin):
    list_display = ('student_roll', 'created_by')
    actions = None

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()


admin.site.register(ExamType)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Result, ResultAdmin)

