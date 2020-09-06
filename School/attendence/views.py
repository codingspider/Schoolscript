from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from subject.models import Class, Group, Subject, Shift, Section

from student.models import Student

from attendence.models import Attendance


def AttendenceListView(request):

    class_list = Class.objects.all()
    group = Group.objects.all()
    shift = Shift.objects.all()
    subject = Subject.objects.all()
    section = Section.objects.all()
    context = {
        'subjects': subject,
        'classes': class_list,
        'groups': group,
        'shifts': shift,
        'section': section
    }
    return render(request, 'attendence/index.html', context)


# class StudentListView(View):
#
#     def post(self, request):
#         if request.method == 'POST':
#             class_id = request.POST.get('class_id')
#             shift_id = request.POST.get('shift_id')
#             section_id = request.POST.get('section_id')
#             group_id = request.POST.get('group_id')
#             date = request.POST.get('date')
#             subject_id = request.POST.get('subject_id')
#
#             if class_id and shift_id and section_id and group_id:
#                 students = Student.objects.filter(student_class_id=class_id, shift_id=shift_id, section_id=section_id,
#                                                   group_id=group_id)
#                 classes = Class.objects.all()
#                 sections = Section.objects.all()
#                 groups = Group.objects.all()
#                 shifts = Shift.objects.all()
#                 subject = Subject.objects.all()
#
#                 context = {
#                     'students': students,
#                     'classes': classes,
#                     'sections': sections,
#                     'groups': groups,
#                     'shifts': shifts,
#                     'subject': subject,
#                     'date': date,
#                     'subject_id': subject_id
#                 }
#                 return render(request, 'attendence/student.html', context)
#             else:
#                 message = "please fill all the field"
#                 return render(request, 'attendence/index.html', message)
#
#         else:
#             message = "please fill all the field"
#             return render(request, 'attendence/index.html', message)

class StudentListView(View):
    def post(self, request):
        if request.method == 'POST' and request.POST:
            class_id = request.POST.get('class_id')
            shift_id = request.POST.get('shift_id')
            section_id = request.POST.get('section_id')
            group_id = request.POST.get('group_id')
            date = request.POST.get('date')
            subject_id = request.POST.get('subject_id')

            students = Student.objects.filter(student_class_id=class_id, shift_id=shift_id, section_id=section_id,
                                              group_id=group_id)

            classes = Class.objects.all()
            sections = Section.objects.all()
            groups = Group.objects.all()
            shifts = Shift.objects.all()
            context = {
                'students': students,
                'classes': classes,
                'section': sections,
                'groups': groups,
                'shifts': shifts,
                'class_id': class_id,
                'date': date,
                'subject_id': subject_id,
                'shift_id': shift_id,
                'section_id': section_id,
                'group_id': group_id,
            }
            return render(request, 'attendence/index.html', context)
        else:
            message = "please fill all the field"
            return render(request, 'attendence/index.html', message)


class AttendanceSaveView(View):
    model = Attendance

    def attendance(self, request):
        data = request.POST
        date = data.get('day', '')
        classes = data.get('classes', '')
        section = data.get('section', '')

        person = Attendance.objects.create(
        date=date, class_id=classes, section=section,

        )
        person.save()


