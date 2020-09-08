from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Syllabus
from .forms import SyllabusForm


class SyllabusListView(ListView):
    model = Syllabus
    context_object_name = 'types'
    form_class = SyllabusForm
    initial = {'key': 'value'}
    template_name = 'syllabus/index.html'

    def get(self, request):
        syllabus = Syllabus.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'syllabus': syllabus, 'form': form}
        return render(request, self.template_name, context)


class SyllabusAddView(CreateView):
    model = Syllabus
    form_class = SyllabusForm
    template_name = 'syllabus/create.html'
    success_url = reverse_lazy('syllabus')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class SyllabusEditView(UpdateView):
    model = Syllabus
    template_name = 'syllabus/update.html'
    context_object_name = 'syllabus'
    form_class = SyllabusForm
    success_url = reverse_lazy('syllabus')


class SyllabusUpdateView(View):
    form_class = SyllabusForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            syllabus = Syllabus.objects.get(pk=request.POST.get('syllabus_id'))
            syllabus.title = request.POST.get('title')
            syllabus.section_id = request.POST.get('section', )
            syllabus.classes_id = request.POST.get('classes', )
            syllabus.subject_id = request.POST.get('subject', )
            syllabus.note = request.POST.get('note', )
            syllabus.file = request.FILES.get('file', )
            syllabus.save()
            return JsonResponse({"instance": 'messages'}, status=200)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class SyllabusDeleteView(DeleteView):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Syllabus.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)








