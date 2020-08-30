from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from ..models import Holiday
from ..form import HolidayForm
from django.contrib import messages
import datetime
from django.utils import formats


# Create your views here.

class HolidayView(View):
    def get(self,request):
        holiday=Holiday.objects.all().order_by('-id')
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        contex = {'holiday': holiday,'date':date}
        return render(request, 'holiday/index.html',contex)


class AddHolidayView(CreateView):
    model = Holiday
    form_class = HolidayForm
    template_name = 'holiday/create.html'
    success_url = reverse_lazy('holidays')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return JsonResponse({"instance": 'success'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DetailHolidayView(View):
    def get(self,request,pk):
        holiday=Holiday.objects.get(id=pk)
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        context={'holiday':holiday,'date':date}
        return render(request, 'holiday/detail.html',context)


class EditHolidayView(UpdateView):
    model = Holiday
    template_name = 'holiday/update.html'
    context_object_name = 'holiday'
    fields = ('title', 'start_date', 'end_date', 'description', 'attachment',)
    success_url = reverse_lazy('holidays')


class UpdateHolidayView(View):
    form_class = HolidayForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            rooms = Holiday.objects.get(pk=request.POST.get('holiday_id'))
            rooms.title = request.POST.get('title')
            rooms.start_date = request.POST.get('start_date', )
            rooms.end_date = request.POST.get('end_date', )
            rooms.description = request.POST.get('description', )
            rooms.attachment = request.POST.get('attachment', )
            rooms.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteHolidayView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Holiday.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class ApprovHolidayView(View):
    def get(self,request,pk):
        Holiday.objects.filter(pk=pk).update(approve_status=1)
        messages.success(request,'Data approve successfull',extra_tags='success')
        return redirect(reverse('holiday:list'))

class DeclineHolidayView(View):
    def get(self,request,pk):
        Holiday.objects.filter(pk=pk).update(approve_status=2)
        messages.success(request,'Data decline successfull',extra_tags='success')
        return redirect(reverse('holiday:list'))

