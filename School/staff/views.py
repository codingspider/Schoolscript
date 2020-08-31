from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Professionals, FamilyInformation
from .forms import ProfessionalForm, FamilyInformationForm


class StaffListView(ListView):
    model = Professionals
    context_object_name = 'profession'
    form_class = ProfessionalForm
    initial = {'key': 'value'}
    template_name = 'profession/index.html'


class StaffAddView(View):
    form_class = ProfessionalForm
    # form_class_2 = FamilyInformationForm

    def get(self, request):
        formface = self.form_class()
        # formface_2 = self.form_class_2()

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

