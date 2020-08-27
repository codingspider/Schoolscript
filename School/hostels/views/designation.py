from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView

from ..models import Designation
from ..form import DesignationForm


class IndexView(View):
    template_name = 'designation/index.html'

    def get(self, request):
        designations = Designation.objects.all().order_by('-id')
        context = {'designations': designations}
        return render(request, self.template_name, context)


class AddView(View):
    template_name = 'designation/create.html'

    def get(self, request):
        form = DesignationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        designations=Designation.objects.all().order_by('-id')
        form = DesignationForm()
        if request.method=='POST':
            designation=request.POST
            form = DesignationForm(request.POST)
            if form.is_valid():
                instance = form.save()
                ser_instance = serializers.serialize('json', [instance, ])
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DesignationUpdateView(UpdateView):
    model = Designation
    template_name = 'designation/update.html'
    context_object_name = 'designation'
    fields = ('title', 'description')
    success_url = reverse_lazy('designations')


class DesignationUpdate(View):
    model = Designation
    form_class = DesignationForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            designations = Designation.objects.get(pk=request.POST.get('id_designation'))
            designations.title = request.POST.get('title')
            designations.description = request.POST.get('description', )
            designations.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DesignationDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Designation.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
