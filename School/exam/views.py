from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ExamForm, ResultForm
from .models import *
from subject.models import Class, Section, Group, Shift, Subject, SubjectType
from student.models import Student


class ExamListView(ListView):
    model = Exam
    context_object_name = 'exam'
    form_class = ExamForm
    initial = {'key': 'value'}
    template_name = 'exam/index.html'

    def get(self, request):
        exams = Exam.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'exams': exams, 'form': form}
        return render(request, self.template_name, context)


class ExamAddView(CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'exam/create.html'
    success_url = reverse_lazy('exam-list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class ExamEditView(UpdateView):
    model = Exam
    template_name = 'exam/update.html'
    context_object_name = 'exam'
    form_class = ExamForm
    success_url = reverse_lazy('exam-list')


class RoomUpdate(View):
    form_class = ExamForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            exams = Exam.objects.get(pk=request.POST.get('exam_id'))
            exams.exam_type = request.POST.get('exam_type')
            exams.exaam_class = request.POST.get('exaam_class')
            exams.subject = request.POST.get('subject')
            exams.exam_date = request.POST.get('exam_date')
            exams.start_time = request.POST.get('start_time')
            exams.end_time = request.POST.get('end_time')
            exams.room_no = request.POST.get('room_no')
            exams.description = request.POST.get('description')
            exams.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class ExamDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Exam.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class ExamMarksListView(View):
    def get(self, request):
        classes = Class.objects.all()
        exam = Exam.objects.all()
        sections = Section.objects.all()
        groups = Group.objects.all()
        shifts = Shift.objects.all()
        subjects = Subject.objects.all()
        context = {
            'classes': classes,
            'sections': sections,
            'groups': groups,
            'shifts': shifts,
            'exams': exam,
            'subjects': subjects
        }

        return render(request, 'exam/marks.html', context)


class ExamGetStudentView(View):
    def post(self, request):
        if request.method == 'POST' and request.POST:
            class_id = request.POST.get('class')
            shift_id = request.POST.get('shift')
            section_id = request.POST.get('section')
            group_id = request.POST.get('group')
            exam_id = request.POST.get('exam')
            subject_id = request.POST.get('subject_id')

            subjects = Subject.objects.filter(teacher_id=1)
            students = Student.objects.filter(student_class_id=class_id, shift_id=shift_id, section_id=section_id,
                                              group_id=group_id)
            classes = Class.objects.all()
            sections = Section.objects.all()
            groups = Group.objects.all()
            shifts = Shift.objects.all()
            sub_type = SubjectType.objects.all()
            exams = Exam.objects.all()

            context = {
                'subjects': subjects,
                'students': students,
                'classes': classes,
                'sections': sections,
                'groups': groups,
                'shifts': shifts,
                'exam_id': exam_id,
                'exams': exams,
                'sub_type': sub_type,
                'class_id': class_id,
                'subject_id': request.POST.get('subject_id'),
            }
            return render(request, 'exam/assign_mark.html', context)
        else:
            message = "please fill all the field"
            return render(request, 'exam/assign_mark.html', message)


class AddExamMarkView(View):

    def post(self, request, *args, **kwargs):
        class_id = request.POST.getlist('class_id[]')
        student_roll = request.POST.getlist('class_roll[]')
        subject_type = request.POST.getlist('sub_type[]')
        exam_type = request.POST.getlist('exam_id[]')
        subject_name = request.POST.getlist('subject_name[]')
        subject_id = request.POST.getlist('subject_id[]')
        pass_mark = request.POST.getlist('pass_mark[]')
        cr_mark = request.POST.getlist('cr_mark[]')
        written_mark = request.POST.getlist('written_mark[]')
        mcq_mark = request.POST.getlist('mcq_mark[]')
        pr_mark = request.POST.getlist('practical_mark[]')
        viva_mark = request.POST.getlist('viva_mark[]')
        #
        sub_len = len(student_roll)
        i = 0
        while i < sub_len:
            result = Result()
            result.class_id = class_id[i]
            result.student_roll = student_roll[i]
            result.exam_type = exam_type[i]
            result.subject_type = subject_type[i]
            result.subject_id = subject_id[i]
            result.pass_mark = pass_mark[i]
            result.written_mark = written_mark[i]
            result.mcq_mark = mcq_mark[i]
            result.practical_mark = pr_mark[i]
            result.viva_mark = viva_mark[i]
            result.created_by = request.user
            instance = result.save()
            i += 1

            # ser_instance = serializers.serialize('json', [instance, ])
        return JsonResponse({"instance": 'ser_instance'}, status=200)


class ResultDeleteView(View):
    def get(self, request):
        Result.objects.all().delete()
