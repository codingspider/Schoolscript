from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from ..models import Hostel, HostelType, Room, HostelRoomStudent, HostelStaff, Designation, HostelRoomAssign
from ..form import HostelForm
from django.contrib import messages
# Create your views here.


class HostelListView(ListView):
    model = Hostel
    context_object_name = 'types'
    form_class = HostelForm
    initial = {'key': 'value'}
    template_name = 'hostel/index.html'

    def get(self, request):
        hotels = Hostel.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'hotels': hotels, 'form': form}
        return render(request, self.template_name, context)


class AddHostelView(CreateView):
    model = Hostel
    template_name = 'hostel/create.html'
    fields = (
        'name', 'address', 'history', 'description', 'type', 'room',
    )
    success_url = reverse_lazy('hostels')


class HostelUpdateView(UpdateView):
    model = Hostel
    template_name = 'hostel/edit.html'
    context_object_name = 'institute'
    fields = ('name', 'address', 'history', 'description', 'type', 'room',)

    def get_success_url(self):
        return reverse_lazy('hostels')


class HostelDeleteView(DeleteView):
    def get(self, request, pk):
        hostel_type= Hostel.objects.get(id=pk)
        hostel_type.delete()
        messages.success(request, 'Data delete successful', extra_tags='success')
        return redirect('hostels')


class HostelDetailView(DetailView):
    model = Hostel
    template_name = 'hostel/detail.html'
    context_object_name = 'hostel'


class HostelRoomView(View):
    def get(self, request, pk):
        hostel = Hostel.objects.get(pk=pk)
        hostel_id = hostel.id
        rooms = Room.objects.filter(hostel=hostel_id).all()
        context = {'rooms': rooms, 'hostel_id': pk}
        return render(request, 'hostel/hostel_room.html', context)


class AddHostelRoomView(View):
    def get(self, request, pk):
        hostel=Hostel.objects.all()
        room = Room.objects.all()
        hostel_id = pk
        context={'room': room, 'hostel': hostel, 'hostel_id': hostel_id}
        return render(request, 'hostel/add_room.html', context)


class AddRoomViewHostel(View):
    def post(self, request):
        pk = request.POST.get('pk')
        hostel=Hostel.objects.get()
        room = Room.objects.all()
        if request.method == 'POST':
            if request.POST.getlist('room_id'):
                for row in request.POST.getlist('room_id'):
                    room1 = Room.objects.filter(id=row).get()
                    hostel.room.add(room1)
                messages.success(request, 'Data store successful', extra_tags='success')
                return redirect(reverse('hostels'))
            else:
                messages.success(request, 'please select a room', extra_tags='error')
                return redirect(reverse('hostel.add_room', args=[pk]))
        context={'room':room}
        return render(request, 'hostel/add_room.html',context)


class DeleteHostelRoomView(View):
    def get(self, request, pk, room):
        hostel=HostelRoomAssign.objects.get(id=pk)
        room1=Room.objects.get(id=room)
        hostel.room.remove(room1)
        messages.success(request, 'Data delete successful', extra_tags='success')
        return redirect(reverse('hostel.room', args=[pk]))


class AddStudentView(View):
    def get(self, request, pk, room):
        student = User.objects.all()
        rooms = Room.objects.filter(hostel=pk).all()
        context = {'rooms': rooms, 'student': student, 'hostel_id': pk}
        return render(request, 'hostel/add_student.html', context)


class AssignStudentView(View):
    def post(self, request):
        if request.method == 'POST':
            if not (request.POST.get('room_id') or request.POST.get('hostel_id') or request.POST.get('user_id')):
                messages.success(request, 'please select al the field', extra_tags='error')
                return redirect('list-hostel')
            room = Room.objects.filter(id=request.POST.get('room_id')).get()
            hostel = Hostel.objects.filter(id=request.POST.get('hostel_id')).get()
            room_member = HostelRoomStudent.objects.filter(hostel=hostel, room=room).count()

            if room.number_of_bed <= room_member:
                messages.success(request, 'No space in this room', extra_tags='error')
                return redirect(reverse('hostels'))
            user = User.objects.filter(id=request.POST.get('user_id')).get()
            check_user = HostelRoomStudent.objects.filter(user=user)
            if check_user:
                messages.success(request, 'User Already assigned', extra_tags='error')
                return redirect(reverse('hostels'))
            data = HostelRoomStudent(user=user, room=room, hostel=hostel)
            data.save()
            messages.success(request, 'Data store successful', extra_tags='success')
            return redirect(reverse('hostels'))


class DerectAddStudent(View):
    def get(self, request, pk):
        student = User.objects.all()
        rooms = Room.objects.all()
        context = {'rooms': rooms, 'student': student, 'hostel_id': pk}
        return render(request, 'hostel/add_student.html', context)


class AddStaffView(View):
    def get(self, request, pk):
        staff=User.objects.all()
        designation=Designation.objects.all()
        context={'designation': designation,'staff':staff, 'hostel_id': pk}
        return render(request, 'hostel/add_staff.html', context)


class AssignStaff(View):
    def post(self, request):
        if request.method =='POST':
            if not (request.POST.get('designation') or request.POST.get('hostel_id') or request.POST.get('user_id')):
                messages.success(request,'please select al the field', extra_tags='error')
                return redirect(reverse('hostels'))
            already_exist = HostelStaff.objects.filter(user_id = request.POST.get('user_id'))

            if already_exist:
                messages.success(request, 'User already exist to this hostel', extra_tags='error')
                return redirect(reverse('hostels'))
            designation=Designation.objects.filter(id=request.POST.get('designation')).get()
            hostel=Hostel.objects.filter(id=request.POST.get('hostel_id')).get()
            user=User.objects.filter(id=request.POST.get('user_id')).get()
            data=HostelStaff(user=user, designation=designation,hostel=hostel)
            data.save()
            messages.success(request, 'Data store successful',extra_tags='success')
            return redirect(reverse('hostels'))

