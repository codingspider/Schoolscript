from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView, UpdateView
from .models import Professionals, FamilyInformation
from .forms import ProfessionalForm, FamilyInformationForm, ProfessionalEditForm


class StaffListView(ListView):
    model = Professionals
    context_object_name = 'profession'
    form_class = ProfessionalForm
    initial = {'key': 'value'}
    template_name = 'profession/index.html'


class StaffAddView(View):
    form_class = ProfessionalForm

    def get(self, request):
        formface = self.form_class()
        context = {'form': formface}
        return render(request, 'profession/create.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            ser_instance = instance.id
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class StaffAddParentView(View):
    form_class = FamilyInformationForm

    def get(self, request, pk):
        formface = self.form_class()
        context = {'form_2': formface, 'pk': pk}
        return render(request, 'profession/family_create.html', context)


class AddFamilyInformationView(View):
    form_class = FamilyInformationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])

            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteStaffView(DeleteView):

    def get(self, request):
        id1 = request.GET.get('id', None)
        Professionals.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class EditStaffInformation(UpdateView):
    model = Professionals
    template_name = 'profession/update.html'
    context_object_name = 'profession'
    form_class = ProfessionalEditForm
    success_url = reverse_lazy('professionals-list')


class UpdateStaffInformationView(View):
    form_class = ProfessionalEditForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            staff = Professionals.objects.get(pk=request.POST.get('staff_id'))
            staff.last_name = request.POST.get('last_name')
            staff.first_name = request.POST.get('first_name')
            staff.gender = request.POST.get('gender', )
            staff.designation_id = request.POST.get('designation', )
            staff.work_type = request.POST.get('work_type', )
            staff.monthly_salary = request.POST.get('monthly_salary', )
            staff.special_for = request.POST.get('special_for', )
            staff.educational_qualification = request.POST.get('educational_qualification', )
            staff.special_training = request.POST.get('special_training', )
            staff.joining_date = request.POST.get('joining_date', )
            staff.retirement_date = request.POST.get('retirement_date', )
            staff.index_number = request.POST.get('index_number', )
            staff.mpo_date = request.POST.get('mpo_date', )
            staff.staff_id_no = request.POST.get('staff_id_no', )
            staff.id_staff_access = request.POST.get('staff_access', )
            staff.teacher_phone = request.POST.get('teacher_phone', )
            staff.birth_date = request.POST.get('birth_date', )
            staff.blood_group = request.POST.get('blood_group', )
            staff.religion = request.POST.get('religion', )
            staff.passport = request.POST.get('passport', )
            staff.nid = request.POST.get('nid', )
            staff.last_organizing = request.POST.get('last_organizing', )
            staff.cause_of_leave = request.POST.get('cause_of_leave', )
            staff.institute_address = request.POST.get('institute_address', )
            staff.status = request.POST.get('status', )
            staff.house_number = request.POST.get('house_number', )
            staff.road_number = request.POST.get('road_number', )
            staff.village = request.POST.get('village', )
            staff.post_office = request.POST.get('post_office', )
            staff.union_name = request.POST.get('union_name', )
            staff.thana = request.POST.get('thana', )
            staff.district = request.POST.get('district', )
            staff.post_code = request.POST.get('post_code', )
            staff.id_is_permanent = request.POST.get('is_permanent', )
            staff.per_house_number = request.POST.get('per_house_number', )
            staff.per_road_number = request.POST.get('per_road_number', )
            staff.per_village = request.POST.get('per_village', )
            staff.per_post_office = request.POST.get('per_post_office')
            staff.per_union_name = request.POST.get('per_union_name')
            staff.per_thana = request.POST.get('per_thana')
            staff.per_district = request.POST.get('per_district')
            staff.per_post_code = request.POST.get('per_post_code')
            staff.image = request.FILES.get('image')
            staff.save()
            instance_id = request.POST.get('staff_id')
            return JsonResponse({"instance": instance_id}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})

