from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from ..models import Notice
from ..form import NoticeForm
from django.contrib import messages
import datetime
from django.utils import formats


# Create your views here.

class NoticeView(View):
    def get(self,request):
        notices=Notice.objects.all().order_by('-id')
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        contex = {'notices':notices,'date':date}
        return render(request, 'notice/index.html',contex)


class AddNoticeView(CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notice/create.html'
    success_url = reverse_lazy('notices')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"instance": 'Success'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DetailNoticeView(View):
    def get(self,request,pk):
        notice=Notice.objects.get(id=pk)
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        context={'notice':notice,'date':date}
        return render(request, 'notice/detail.html',context)


class EditNoticeView(UpdateView):
    model = Notice
    template_name = 'notice/update.html'
    context_object_name = 'notice'
    fields = ('title', 'active_date', 'description', 'attachment', 'status',)
    success_url = reverse_lazy('notices')


class UpdateNoticeView(View):
    form_class = NoticeForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            rooms = Notice.objects.get(pk=request.POST.get('notice_id'))
            rooms.title = request.POST.get('title')
            rooms.active_date = request.POST.get('active_date', )
            rooms.description = request.POST.get('description', )
            rooms.attachment = request.FILES.get('attachment', )
            rooms.status = request.POST.get('status', )
            rooms.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteNoticeView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Notice.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class ApprovNoticeView(View):
    def get(self,request,pk):
        Notice.objects.filter(pk=pk).update(approve_status=1)
        messages.success(request,'Data approve successfull',extra_tags='success')
        return redirect(reverse('notice:list'))

class DeclineNoticeView(View):
    def get(self,request,pk):
        Notice.objects.filter(pk=pk).update(approve_status=2)
        messages.success(request,'Data decline successfull',extra_tags='success')
        return redirect(reverse('notice:list'))

