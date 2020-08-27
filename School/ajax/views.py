from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
# Create your views here.
from django.views import View


from .forms import JoinForm
from .mixins import AjaxFormMixin


class JoinFormView(FormView):
    form_class = JoinForm
    template_name  = 'forms/ajax.html'
    success_url = '/institutes'

    def form_invalid(self, form):
        response = super(JoinFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(JoinFormView, self).form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response