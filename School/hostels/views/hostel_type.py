from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, UpdateView

from ..models import HostelType
from ..form import HostelTypeForm
#from .form import *
from django.contrib import messages
# Create your views here.


class AddHostelType(View):
    form_class = HostelTypeForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})



class TypesListView(ListView):
    model = HostelType
    context_object_name = 'types'
    form_class = HostelTypeForm
    initial = {'key': 'value'}
    template_name = 'hosteltype/index.html'

    def get(self, request):
        hostel_types = HostelType.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'hostel_types': hostel_types, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        hostel_types = HostelType.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        hostel_type = request.POST
        form = HostelTypeForm(request.POST)
        if form.is_valid():
            hostel_type = form.save()
            messages.success(request, 'Data store successfull', extra_tags='success')
            return redirect('types')
        context = {'hostel_types': hostel_types, 'form': form}
        return render(request, self.template_name, context)


class EditHostelTypeView(UpdateView):
    model = HostelType
    template_name = 'hosteltype/update.html'
    context_object_name = 'hosteltypes'
    fields = ('type','description',)
    success_url = reverse_lazy('types')


class UpdateHostelTyepView(View):
    model = HostelType
    form_class = HostelTypeForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            hostel_type = HostelType.objects.get(pk=request.POST.get('type_id'))
            hostel_type.type = request.POST.get('type')
            hostel_type.description = request.POST.get('description', )
            hostel_type.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteHostelTypeView(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        HostelType.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)



