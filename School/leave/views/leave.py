from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from ..models import Leave
from ..form import LeaveForm
from django.contrib import messages
# Create your views here.

class LeaveView(View):
    def get(self,request):
        leaves=Leave.objects.all().order_by('-id')
        contex = {'leaves':leaves}
        return render(request, 'leave/index.html',contex)


class AddLeaveView(View):
    def get(self,request):
        form = LeaveForm()
        context = {'form':form}
        return render(request, 'leave/create.html',context)

    def post(self,request):
        request.POST=request.POST.copy()
        request.POST['applied_by']=request.user.id
        # request.POST['role']=1
        form = LeaveForm(request.POST, request.FILES) 
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditLeaveView(UpdateView):
    model = Leave
    template_name = 'leave/update.html'
    context_object_name = 'leave'
    fields = ('role', 'applied_by', 'leave_type', 'apply_date', 'from_date','to_date', 'reason', 'attachment', 'apply_status', 'approve_status', 'approved_by')
    success_url = reverse_lazy('room_list')


class UpdateLeaveView(View):
    form_class = LeaveForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            rooms = Leave.objects.get(pk=request.POST.get('leave_id'))
            rooms.id_leave_type = request.POST.get('leave_type')
            rooms.apply_date = request.POST.get('apply_date', )
            rooms.from_date = request.POST.get('from_date', )
            rooms.to_date = request.POST.get('to_date', )
            rooms.reason = request.POST.get('reason', )
            rooms.attachment = request.FILES.get('attachment', )
            rooms.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})

    

class DeleteLeaveView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Leave.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class ApprovLeaveView(View):
    def get(self,request,pk):
        Leave.objects.filter(pk=pk).update(approve_status=1)
        messages.success(request,'Data approve successfull',extra_tags='success')
        return redirect(reverse('leave:list'))

class DeclineLeaveView(View):
    def get(self,request,pk):
        Leave.objects.filter(pk=pk).update(approve_status=2)
        messages.success(request,'Data decline successfull',extra_tags='success')
        return redirect(reverse('leave:list'))

