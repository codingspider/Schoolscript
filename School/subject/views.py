from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Subject
from .forms import SubjectForm


class SubjectListView(ListView):
    model = Subject
    context_object_name = 'subject'
    form_class = SubjectForm
    initial = {'key': 'value'}
    template_name = 'subject/index.html'

    def get(self, request):
        subjects = Subject.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'subjects': subjects, 'form': form}
        return render(request, self.template_name, context)


class SubjectAddView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject/create.html'
    success_url = reverse_lazy('subjects')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class SubjectEditView(UpdateView):
    model = Subject
    template_name = 'subject/update.html'
    context_object_name = 'room'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects')


class SubjectUpdateView(View):
    form_class = SubjectForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            subject = Subject.objects.get(pk=request.POST.get('subject_id'))
            subject.name = request.POST.get('name')
            subject.description = request.POST.get('description', )
            subject.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class SubjectDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Subject.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


