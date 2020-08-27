from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import ParentForm
from .models import Parent
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView


class ParentListView(ListView):
    def get(self, request):
        parents = Parent.objects.all()
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


class ParentUpdateView(UpdateView):

    model = Parent
    template_name = 'parent/update.html'
    context_object_name = 'parent'
    fields = ('father_name', 'father_occupation', 'father_monthly_income','educational_qualification', 'father_phone', 'father_email', 'father_nid', 'father_passport',
        'father_license', 'mother_name', 'mother_occupation', 'mother_monthly_income', 'mother_educational_qualification', 'mother_phone', 'mother_email', 'mother_nid',
        'mother_passport', 'mother_license', )

    def get_success_url(self):
        return reverse_lazy('parent-list')


class ParentDetailView(DetailView):
    def get(self, request, pk):
        parent = Parent.objects.filter(id=pk)
        return render(request, 'parent/detail.html', {'parent': parent})


class DeleteParentView(View):
    def get(self, request, pk):
        hostel=Parent.objects.get(id=pk)
        hostel.delete()
        messages.success(request, 'Data delete successfull', extra_tags='success')
        return redirect('parent-list/')






