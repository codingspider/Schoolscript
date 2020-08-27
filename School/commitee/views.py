from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView

from .forms import CommitteeForm
from .models import Commitee


class CommiteeListView(View):
    def get(self, request):
        committees = Commitee.objects.all()
        return render(request, 'commitee/index.html', {'committees': committees})


class CommiteeAddView(View):
    model = Commitee
    context_object_name = 'committee'
    form_class = CommitteeForm
    initial = {'key': 'value'}
    template_name = 'commitee/create.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CommitteeForm()
        if request.method == 'POST':
            form = CommitteeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Data added successful', extra_tags='success')
                return redirect('add_committee')
        context = {'form': form}
        return render(request, self.template_name, context)


class CommiteeDetailView(View):
    def get(self, request, pk):
        committees = Commitee.objects.get(pk = pk)
        return render(request, 'commitee/detail.html', {'committees': committees})


class CommiteeUpdateView(UpdateView):
    model = Commitee
    template_name = 'commitee/update.html'
    context_object_name = 'teacher'
    fields = ('full_name', 'gender', 'designation', 'educational_qualification','joining_date', 'expire_date', 'email', 'password', 'phone', 'dob',
              'blood_group', 'religion', 'passport', 'nid', 'village',
              'post', 'union', 'upozilla', 'district', 'postal_code', 'image'
              )

    def get_success_url(self):
        return reverse_lazy('committees')


class CommiteeDeleteView(DeleteView):
    def get(self, request, pk):
        committee = Commitee.objects.get(id=pk)
        committee.delete()
        messages.success(request, 'Data delete successfull', extra_tags='success')
        return redirect('committees')
