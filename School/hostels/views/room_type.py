from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from ..models import Room, RoomType
from ..form import RoomForm, RoomTypeForm


class TypeCreateView(CreateView):
    model = RoomType
    template_name = 'roomtype/create.html'
    form_class = RoomTypeForm
    success_url = reverse_lazy('room_types_list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class RoomTypeListView(ListView):
    model = RoomType
    context_object_name = 'types'
    form_class = RoomForm
    initial = {'key': 'value'}
    template_name = 'roomtype/index.html'

    def get(self, request):
        room_types = RoomType.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'room_types': room_types, 'form': form}
        return render(request, self.template_name, context)


class RoomTypeUpdateView(UpdateView):
    model = RoomType
    template_name = 'roomtype/update.html'
    context_object_name = 'room'
    fields = ( 'type', 'description',)
    success_url = reverse_lazy('room_types_list')


class RoomTypeUpdate(View):
    model = RoomType
    form_class = RoomTypeForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            room_type = RoomType.objects.get(pk=request.POST.get('room_id'))
            room_type.type = request.POST.get('type')
            room_type.description = request.POST.get('description', )
            room_type.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class RoomTypeDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        RoomType.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


