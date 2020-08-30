from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from ..models import Vehicle,Driver
from ..form import VehicleForm
from django.contrib import messages
# Create your views here.


class VehiclesView(View):
    def get(self,request):
        vehicles=Vehicle.objects.all().order_by('-id')
        contex = {'vehicles':vehicles}
        return render(request, 'vehicle/index.html', contex)


class AddVehicleView(View):
    def get(self, request):
        form = VehicleForm()
        context = {'form':form}
        return render(request, 'vehicle/create.html', context)

    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle/create.html'
    success_url = reverse_lazy('vehicles')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditVehicleView(UpdateView):
    model = Vehicle
    template_name = 'vehicle/update.html'
    context_object_name = 'vehicle'
    fields = ('name', 'number', 'model', 'license', 'year_made', 'driver', 'description')
    success_url = reverse_lazy('vehicles')


class VehicleUpdate(View):
    form_class = VehicleForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            vehicle = Vehicle.objects.get(pk=request.POST.get('vehicle_id'))
            vehicle.name = request.POST.get('name')
            vehicle.number = request.POST.get('number', )
            vehicle.model = request.POST.get('model', )
            vehicle.license = request.POST.get('license', )
            vehicle.year_made = request.POST.get('year_made', )
            # vehicle.driver = request.POST.get('driver', )
            vehicle.description = request.POST.get('description', )
            vehicle.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteVehicleView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Vehicle.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)



class VehicleDriversView(View):
    def get(self,request,pk):
        drivers=Driver.objects.filter(vehicle=pk).all()
        contex = {'drivers':drivers,'vehicle':pk}
        return render(request, 'vehicle/driver.html',contex)


class AddVehicleDriverView(View):
    def get(self,request,pk):
        vehicle=Vehicle.objects.get(id=pk)
        driver = Driver.objects.all()
        context={'driver':driver}
        return render(request, 'vehicle/add_driver.html', context)

    def post(self, request, pk):
        vehicle= Vehicle.objects.get(id=pk)
        if request.method == 'POST':
            if request.POST.getlist('driver_id'):
                for row in request.POST.getlist('driver_id'):
                    driver1 = Driver.objects.filter(id=row).get()
                    vehicle.driver.add(driver1)
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('transport:vehicle_drivers', args=[pk]))
            else:
                messages.success(request,'please select a driver',extra_tags='error')
                return redirect(reverse('transport:add_vehicle_driver', args=[pk]))
    

class DeleteVehicleDriverView(View):
    def get(self,request,vehicle,driver):
        hostel=Vehicle.objects.get(id=vehicle)
        driver=Driver.objects.get(id=driver)
        hostel.driver.remove(driver)
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('transport:vehicle_drivers', args=[vehicle]))


class GetDriverView(View):
    def get(self,request):
        vehicle=request.GET.get('vehicle')
        drivers=Driver.objects.filter(vehicle=vehicle).all()
        context={'drivers':drivers}
        return render(request, 'schedule/get_driver.html',context)