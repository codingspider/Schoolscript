from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView

from .forms import TeacherForm
from .models import Teacher


class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request, 'teacher/index.html', {'teachers': teachers})


class TeacherAddView(View):
    model = Teacher
    context_object_name = 'student'
    form_class = TeacherForm
    initial = {'key': 'value'}
    template_name = 'teacher/create.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = TeacherForm()
        if request.method == 'POST':
            form = TeacherForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save()
                ser_instance = serializers.serialize('json', [instance, ])
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class TeacherDetailView(View):
    def get(self, request, pk):
        teachers = Teacher.objects.get(pk = pk)
        return render(request, 'teacher/detail.html', {'teachers': teachers})


class TeacherEditView(UpdateView):
    model = Teacher
    template_name = 'teacher/update.html'
    context_object_name = 'teacher'
    fields = ('full_name', 'gender', 'teacher_designation', 'work_type', 'monthly_salary', 'special_for',
              'educational_qualification', 'special_training', 'joining_date', 'retirement_date', 'index_number', 'mpo_date', 'staff_id_no',
              'staff_access', 'teacher_email', 'teacher_password', 'teacher_phone', 'teacher_dob',
              'blood_group', 'religion', 'passport', 'nid', 'last_organizing', 'cause_of_leave', 'institute_address', 'village',
              'post', 'union', 'upozilla', 'district', 'postal_code','permanent_upozilla', 'permanent_district', 'permanent_postal_code',
              'permanent_village', 'permanent_post', 'permanent_union', 'father_name', 'father_occupation', 'father_monthly_income', 'father_qualification', 'father_phone',
              'father_email', 'father_nid', 'father_passport', 'father_license', 'mother_name', 'mother_occupation', 'mother_monthly_income',
              'mother_educational_qualification', 'mother_phone', 'mother_email', 'mother_nid', 'mother_passport', 'mother_license', 'spouse_name',
              'spouse_occupation', 'marrige_day', 'spouse_education', 'kids', 'image'

              )

    def get_success_url(self):
        return reverse_lazy('teachers')


class TeacherUpdateView(View):
    form_class = TeacherForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            teacher = Teacher.objects.get(pk=request.POST.get('teacher_id'))
            teacher.full_name = request.POST.get('full_name')
            teacher.gender = request.POST.get('gender', )
            teacher.teacher_designation = request.POST.get('teacher_designation', )
            teacher.work_type = request.POST.get('work_type', )
            teacher.monthly_salary = request.POST.get('monthly_salary', )
            teacher.special_for = request.POST.get('special_for', )
            teacher.educational_qualification = request.POST.get('educational_qualification', )
            teacher.special_training = request.POST.get('special_training', )
            teacher.joining_date = request.POST.get('joining_date', )
            teacher.retirement_date = request.POST.get('retirement_date', )
            teacher.index_number = request.POST.get('index_number', )
            teacher.mpo_date = request.POST.get('mpo_date', )
            teacher.staff_id_no = request.POST.get('staff_id_no', )
            teacher.staff_access = request.POST.get('staff_access', )
            teacher.teacher_email = request.POST.get('teacher_email', )
            teacher.teacher_password = request.POST.get('teacher_password', )
            teacher.teacher_phone = request.POST.get('teacher_phone', )
            teacher.teacher_dob = request.POST.get('teacher_dob', )
            teacher.blood_group = request.POST.get('blood_group', )
            teacher.religion = request.POST.get('religion', )
            teacher.passport = request.POST.get('passport', )
            teacher.nid = request.POST.get('nid', )
            teacher.last_organizing = request.POST.get('last_organizing', )
            teacher.cause_of_leave = request.POST.get('cause_of_leave', )
            teacher.institute_address = request.POST.get('institute_address', )
            teacher.village = request.POST.get('village', )
            teacher.post = request.POST.get('post', )
            teacher.union = request.POST.get('union', )
            teacher.upozilla = request.POST.get('upozilla', )
            teacher.district = request.POST.get('district', )
            teacher.postal_code = request.POST.get('postal_code', )
            teacher.permanent_upozilla = request.POST.get('permanent_upozilla', )
            teacher.permanent_district = request.POST.get('permanent_district', )
            teacher.permanent_postal_code = request.POST.get('permanent_postal_code', )
            teacher.permanent_village = request.POST.get('permanent_village', )
            teacher.permanent_post = request.POST.get('permanent_post', )
            teacher.permanent_union = request.POST.get('permanent_union', )
            teacher.father_name = request.POST.get('father_name', )
            teacher.father_occupation = request.POST.get('father_occupation', )
            teacher.father_monthly_income = request.POST.get('father_monthly_income', )
            teacher.father_qualification = request.POST.get('father_qualification', )
            teacher.father_phone = request.POST.get('father_phone', )
            teacher.father_email = request.POST.get('father_email', )
            teacher.father_nid = request.POST.get('father_nid', )
            teacher.father_passport = request.POST.get('father_passport', )
            teacher.father_license = request.POST.get('father_license', )
            teacher.father_name = request.POST.get('father_name', )
            teacher.father_occupation = request.POST.get('father_occupation', )
            teacher.father_monthly_income = request.POST.get('father_monthly_income', )
            teacher.father_qualification = request.POST.get('father_qualification', )
            teacher.father_phone = request.POST.get('father_phone', )
            teacher.father_email = request.POST.get('father_email', )
            teacher.father_nid = request.POST.get('father_nid', )
            teacher.father_passport = request.POST.get('father_passport', )
            teacher.spouse_name = request.POST.get('spouse_name', )
            teacher.spouse_qualification = request.POST.get('spouse_qualification', )
            teacher.kids = request.POST.get('kids', )
            teacher.image = request.POST.get('image', )
            teacher.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class TeacherDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Teacher.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
