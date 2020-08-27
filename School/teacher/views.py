from django.contrib import messages
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
                form.save()
                messages.success(request, 'Data added successful', extra_tags='success')
                return redirect('add-teacher')
        context = {'form': form}
        return render(request, self.template_name, context)


class TeacherDetailView(View):
    def get(self, request, pk):
        teachers = Teacher.objects.get(pk = pk)
        return render(request, 'teacher/detail.html', {'teachers': teachers})


class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teacher/update.html'
    context_object_name = 'teacher'
    fields = ('full_name', 'gender', 'teacher_designation', 'work_type', 'monthly_salary', 'special_for',
              'educational_qualification', 'special_training', 'joining_date', 'retirement_date', 'index_number', 'mpo_date', 'staff_id_no',
              'staff_access', 'teacher_email', 'teacher_password', 'teacher_phone', 'teacher_dob',
              'blood_group', 'religion', 'passport', 'nid', 'last_organizing', 'cause_of_leave', 'institute_address', 'village',
              'post', 'union', 'upozilla', 'district', 'postal_code','permanent_upozilla', 'permanent_district', 'permanent_postal_code',
              'permanent_village', 'permanent_post', 'permanent_union', 'father_name', 'father_occupation', 'permanent_upozilla', 'permanent_district',
              'permanent_postal_code', 'father_name', 'father_occupation', 'father_monthly_income', 'father_qualification', 'father_phone',
              'father_email', 'father_nid', 'father_passport', 'father_license', 'mother_name', 'mother_occupation', 'mother_monthly_income',
              'mother_educational_qualification', 'mother_phone', 'mother_email', 'mother_nid', 'mother_passport', 'mother_license', 'spouse_name',
              'spouse_occupation', 'marrige_day', 'spouse_education', 'kids', 'image'

              )

    def get_success_url(self):
        return reverse_lazy('teachers')


class TeacherDeleteView(DeleteView):
    def get(self, request, pk):
        student=Teacher.objects.get(id=pk)
        student.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect('teachers')