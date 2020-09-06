from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView
from django.core import serializers
from .forms import StudentForm
from .models import Student


class StudentAddView(View):
    model = Student
    context_object_name = 'student'
    form_class = StudentForm
    initial = {'key': 'value'}
    template_name = 'student/create.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'student/list.html', {'students': students})


class StudentDetailsView(View):
    def get(self, request, pk):
        students = Student.objects.filter(pk=pk)
        return render(request, 'student/detail.html', {'students': students})


class StudentEditView(UpdateView):
    model = Student
    template_name = 'student/update.html'
    context_object_name = 'institute'
    form_class = StudentForm

    def get_success_url(self):
        return reverse_lazy('students')


class StudentUpdateView(View):
    form_class = StudentForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            student = Student.objects.get(pk=request.POST.get('student_id'))
            student.institute_name = request.POST.get('institute_name')
            student.student_name = request.POST.get('student_name', )
            student.gender = request.POST.get('gender', )
            student.student_class_id = request.POST.get('student_class',)
            student.shift_id = request.POST.get('shift', )
            student.section_id = request.POST.get('section', )
            student.group_id = request.POST.get('group', )
            student.id_number = request.POST.get('id_number', )
            student.class_roll = request.POST.get('class_roll', )
            student.session = request.POST.get('session', )
            student.dob = request.POST.get('dob', )
            student.blood_group = request.POST.get('blood_group', )
            student.religion = request.POST.get('religion', )
            student.birth_id_number = request.POST.get('birth_id_number', )
            student.phone_number = request.POST.get('phone_number', )
            student.email = request.POST.get('email', )
            student.old_school_address = request.POST.get('old_school_address', )
            student.cause_for_leave = request.POST.get('cause_for_leave', )
            student.house_no = request.POST.get('house_no', )
            student.house_name = request.POST.get('house_name', )
            student.road_no = request.POST.get('road_no', )
            student.village = request.POST.get('village', )
            student.post = request.POST.get('post', )
            student.union = request.POST.get('union', )
            student.upozilla = request.POST.get('upozilla', )
            student.district = request.POST.get('district', )
            student.postal_code = request.POST.get('postal_code', )
            student.permanent_village = request.POST.get('permanent_village', )
            student.permanent_post = request.POST.get('permanent_post', )
            student.permanent_union = request.POST.get('permanent_union', )
            student.permanent_upozilla = request.POST.get('permanent_upozilla', )
            student.permanent_district = request.POST.get('permanent_district', )
            student.permanent_postal_code = request.POST.get('permanent_postal_code', )
            student.student_image = request.FILES.get('student_image', )
            student.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class StudentDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Student.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


