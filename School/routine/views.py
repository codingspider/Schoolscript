from django.db.models import Count, QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import TimeTableItem
from .forms import TimeTableItemForm
from subject.models import Class

from teacher.models import Teacher


class RoutineListView(ListView):
    model = TimeTableItem
    context_object_name = 'types'
    form_class = TimeTableItemForm
    initial = {'key': 'value'}
    template_name = 'routine/index.html'

    def get(self, request):
        results = TimeTableItem.objects.all()
        form = self.form_class(initial=self.initial)
        classes = Class.objects.all()

        context = {
            'routines': results,
            'form': form,
            'classes': classes,

        }
        return render(request, self.template_name, context)

