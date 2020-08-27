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


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/update.html'
    context_object_name = 'institute'
    fields = ('institute_name', 'student_name', 'gender', 'student_class', 'shift', 'section',
              'group', 'id_number', 'class_roll', 'session', 'dob', 'blood_group', 'religion',
              'birth_id_number', 'phone_number', 'email', 'old_school_address', 'cause_for_leave',
              'house_no', 'house_name', 'road_no', 'village', 'post', 'union', 'upozilla', 'district',
              'postal_code', 'permanent_village', 'permanent_post', 'permanent_union', 'permanent_upozilla',
              'permanent_district', 'permanent_postal_code', 'image'

              )

    def get_success_url(self):
        return reverse_lazy('students')


class StudentDeleteView(DeleteView):
    def get(self, request, pk):
        student=Student.objects.get(id=pk)
        student.delete()
        messages.success(request,'Data delete successful',extra_tags='success')
        return redirect('students')

