from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from ..models import Driver
from ..form import DriverForm
from django.contrib import messages
# Create your views here.

class DriversView(View):
    def get(self,request):
        drivers=Driver.objects.all().order_by('-id')
        contex = {'drivers':drivers}
        return render(request, 'driver/index.html',contex)


class AddDriverView(CreateView):
    model = Driver
    form_class = DriverForm
    template_name = 'driver/create.html'
    success_url = reverse_lazy('drivers')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditDriverView(UpdateView):
    model = Driver
    template_name = 'driver/update.html'
    context_object_name = 'driver'
    fields = ('name', 'phone', 'driving_licence', 'driving_licence_validity', 'age', 'gender', 'address')
    success_url = reverse_lazy('drivers')


class DriverUpdateView(View):
    form_class = DriverForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            rooms = Driver.objects.get(pk=request.POST.get('driver_id'))
            rooms.name = request.POST.get('name')
            rooms.phone = request.POST.get('phone', )
            rooms.driving_licence = request.POST.get('driving_licence', )
            rooms.driving_licence_validity = request.POST.get('driving_licence_validity', )
            rooms.age = request.POST.get('age', )
            rooms.gender = request.POST.get('gender', )
            rooms.address = request.POST.get('address', )
            rooms.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteDriverView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Driver.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

