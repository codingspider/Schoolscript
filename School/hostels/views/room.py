from django.contrib import messages
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from ..models import Room, RoomType
from ..form import RoomForm


class AddRoomView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'room/create.html'
    success_url = reverse_lazy('room_list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})



class RoomListView(ListView):
    model = Room
    context_object_name = 'types'
    form_class = RoomForm
    initial = {'key': 'value'}
    template_name = 'room/index.html'

    def get(self, request):
        rooms = Room.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'rooms': rooms, 'form': form}
        return render(request, self.template_name, context)


class RoomUpdateView(UpdateView):
    model = Room
    template_name = 'room/update.html'
    context_object_name = 'room'
    fields = ('number', 'number_of_bed', 'bed_cost', 'type', 'description',)
    success_url = reverse_lazy('room_list')


class RoomUpdate(View):
    form_class = RoomForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            rooms = Room.objects.get(pk=request.POST.get('room_id'))
            rooms.number = request.POST.get('number')
            rooms.number_of_bed = request.POST.get('number_of_bed', )
            rooms.bed_cost = request.POST.get('bed_cost', )
            rooms.room_type = request.POST.get('room_type', )
            rooms.description = request.POST.get('description', )
            rooms.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class RoomDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Room.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


