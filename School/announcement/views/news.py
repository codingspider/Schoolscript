from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from ..models import News
from ..form import NewsForm
from django.contrib import messages
import datetime
from django.utils import formats


# Create your views here.

class NewsView(View):

    def get(self,request):
        news=News.objects.all().order_by('-id')
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        contex = {'news':news,'date':date}
        return render(request, 'news/index.html',contex)


class AddNewsView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/create.html'
    success_url = reverse_lazy('news')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DetailNewsView(View):
    def get(self, request, pk):
        news= News.objects.get(id=pk)
        date= formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        context= {'news':news,'date':date}
        return render(request, 'news/detail.html',context)

class EditNewsView(View):
    def get(self,request,pk):
        news=News.objects.get(id=pk)
        form = NewsForm(instance=news)
        context={'form':form}
        return render(request, 'news/create.html',context)
    def post(self,request,pk):
        news=News.objects.get(id=pk)
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request,'Data update successfull',extra_tags='success')
            return redirect(reverse('announcement:news'))
    

class NewsDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        News.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class ApprovNewsView(View):
    def get(self,request,pk):
        News.objects.filter(pk=pk).update(approve_status=1)
        messages.success(request,'Data approve successfull',extra_tags='success')
        return redirect(reverse('news:list'))

class DeclineNewsView(View):
    def get(self,request,pk):
        News.objects.filter(pk=pk).update(approve_status=2)
        messages.success(request,'Data decline successfull',extra_tags='success')
        return redirect(reverse('news:list'))

