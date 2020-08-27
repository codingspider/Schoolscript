import datetime
import os

from django.conf import settings
from django.contrib import messages
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import AddInstituteForm, InstituteImageUpdate
from .models import Institute, City, State, Country, MonthlyWeatherByCity


class AllInstituteView(ListView):
    model = Institute
    template_name = 'institute/list.html'
    context_object_name = 'institute'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(AllInstituteView, self).get_context_data(**kwargs)
        books = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(books, self.paginate_by)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context['books'] = books
        return context


class InstituteEditView(UpdateView):
    model = Institute
    template_name = 'institute/update.html'
    context_object_name = 'institute'
    fields = ('name', 'website', 'email_1', 'email_2', 'institute_code', 'address_1','country', 'state', 'city','zip', 'latitude', 'longitude',
              'address_2', 'established_date', 'phone_1', 'phone_2', 'fax', 'active_status','institute_logo', 'principle_signature', 'agree',)

    def get_success_url(self):
        return reverse_lazy('institute_detail', kwargs={'pk': self.object.id})


class InstituteDetailView(DetailView):
    model = Institute
    template_name = 'institute/detail.html'
    context_object_name = 'institute'


class InstituteDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Institute.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


def load_state(request):
    country_id = request.GET.get('country')
    state_id = State.objects.filter(country_id=country_id)
    return render(request, 'institute/city_dropdown_list_options.html', {'state': state_id})


def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id)
    return render(request, 'institute/city_dropdown_list_options.html', {'cities': cities})


class EditInstituteView(View):
    def post(self, request):
        Institute.objects.filter(pk=request.POST.get('institute_id')).update(
            name=request.POST.get('name'),
            email_1=request.POST.get('email_1'),
            email_2=request.POST.get('email_2'),
            website=request.POST.get('website', ''),
            institute_code=request.POST.get('institute_code', ''),
            # country=request.POST.get('country', ''),
            # # state=request.POST.get('state', ''),
            # # city=request.POST.get('city', ''),
            zip=request.POST.get('zip', ''),
            latitude=request.POST.get('latitude', ''),
            longitude=request.POST.get('longitude', ''),
            address_1=request.POST.get('address_1', ''),
            address_2=request.POST.get('address_2', ''),
            phone_1=request.POST.get('phone_1', ''),
            phone_2=request.POST.get('phone_2', ''),
            fax=request.POST.get('fax', ''),
            agree=request.POST.get('agree', ''),
            established_date=request.POST.get('established_date', ''),

        )

        return JsonResponse({"success": 'Message'}, status=200)


class InstituteImageEdit(View):
    model = Institute
    form_class = InstituteImageUpdate

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            user_profile = Institute.objects.get(pk=request.POST.get('institute_id'))
            user_profile.institute_logo = request.FILES.get('institute_logo')
            user_profile.principle_signature = request.FILES.get('principle_signature', )
            user_profile.save()

            # Institute.objects.filter(pk=request.POST.get('institute_id')).update(
            #
            #     institute_logo=request.FILES.get('institute_logo', ),
            #     principle_signature=request.FILES.get('principle_signature', ),
            # )
            # form.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class AddInstituteView(View):
    model = Institute
    context_object_name = 'types'
    form_class = AddInstituteForm
    initial = {'key': 'value'}
    template_name = 'institute/create.html'

    def get(self, request):
        formface = self.form_class(initial=self.initial)
        context = {'form': formface}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})



