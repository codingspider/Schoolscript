from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import ParentForm
from staff.models import FamilyInformation
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from staff.forms import FamilyInformationForm


class ParentListView(ListView):
    def get(self, request):
        parents = FamilyInformation.objects.all()
        return render(request, "parent/index.html", {'parents': parents})


class ParentAddView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        form = ParentForm()
        context['form'] = form
        return render(request, "parent/create.html", context)

    def post(self, request):
        if request.method == 'POST':
            form = ParentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(self.request, 'Form submission successful')
        else:
            form = ParentForm()
        return render(request, "parent/create.html", {'form': form})


class ParentEditView(UpdateView):

    model = FamilyInformation
    template_name = 'parent/update.html'
    context_object_name = 'parent'
    form_class = FamilyInformationForm

    def get_success_url(self):
        return reverse_lazy('parent-list')


class ParentUpdateView(View):
    form_class = FamilyInformationForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            family = FamilyInformation.objects.get(pk=request.POST.get('family_id'))
            family.father_name = request.POST.get('father_name')
            family.father_occupation = request.POST.get('father_occupation')
            family.father_monthly_income = request.POST.get('father_monthly_income')
            family.father_qualification = request.POST.get('father_qualification')
            family.father_phone = request.POST.get('father_phone')
            family.father_email = request.POST.get('father_email')
            family.father_nid = request.POST.get('father_nid')
            family.father_passport = request.POST.get('father_passport')
            family.father_license = request.POST.get('father_license')
            family.mother_name = request.POST.get('mother_name')
            family.mother_occupation = request.POST.get('mother_occupation')
            family.mother_monthly_income = request.POST.get('mother_monthly_income')
            family.mother_educational_qualification = request.POST.get('mother_educational_qualification')
            family.mother_phone = request.POST.get('mother_phone')
            family.mother_email = request.POST.get('mother_email')
            family.mother_nid = request.POST.get('mother_nid')
            family.mother_passport = request.POST.get('mother_passport')
            family.mother_license = request.POST.get('mother_license')
            family.nid = request.POST.get('nid')
            family.spouse_name = request.POST.get('spouse_name')
            family.spouse_occupation = request.POST.get('spouse_occupation')
            family.marrige_day = request.POST.get('marrige_day')
            family.spouse_education = request.POST.get('spouse_education')
            family.kids = request.POST.get('kids')

            family.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class ParentDetailView(DetailView):
    def get(self, request, pk):
        parent = FamilyInformation.objects.filter(id=pk)
        return render(request, 'parent/detail.html', {'parent': parent})


class DeleteParentView(View):
    def get(self, request, pk):
        hostel=FamilyInformation.objects.get(id=pk)
        hostel.delete()
        messages.success(request, 'Data delete successfull', extra_tags='success')
        return redirect('parent-list/')






