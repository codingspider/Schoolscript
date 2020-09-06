from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView
from .forms import LocationForm
from .models import PointOfInterest
# from .models import Photo, CrudUser
# from .forms import PhotoForm, GeoForm


# def photo_list(request):
#     photos = Photo.objects.all()
#     if request.method == 'POST':
#         form = PhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('photo_list')
#     else:
#         form = PhotoForm()
#     return render(request, 'album/photo_list.html', {'form': form, 'photos': photos})
#
#
# class CrudView(TemplateView):
#     template_name = 'album/crud.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['users'] = CrudUser.objects.all()
#         return context
#
#
# class CreateCrudUser(View):
#     def  get(self, request):
#         name1 = request.GET.get('name', None)
#         address1 = request.GET.get('address', None)
#         age1 = request.GET.get('age', None)
#
#         obj = CrudUser.objects.create(
#             name = name1,
#             address = address1,
#             age = age1
#         )
#
#         user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}
#
#         data = {
#             'user': user
#         }
#         return JsonResponse(data)
#
# class DeleteCrudUser(View):
#     def  get(self, request):
#         id1 = request.GET.get('id', None)
#         CrudUser.objects.get(id=id1).delete()
#         data = {
#             'deleted': True
#         }
#         return JsonResponse(data)
#
#
# class UpdateCrudUser(View):
#     def  get(self, request):
#         id1 = request.GET.get('id', None)
#         name1 = request.GET.get('name', None)
#         address1 = request.GET.get('address', None)
#         age1 = request.GET.get('age', None)
#
#         obj = CrudUser.objects.get(id=id1)
#         obj.name = name1
#         obj.address = address1
#         obj.age = age1
#         obj.save()
#
#         user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}
#
#         data = {
#             'user': user
#         }
#         return JsonResponse(data)


class GeoPostion(View):
    def get(self, request):
        return render(request, 'album/geo.html')


class AddPostionMap(View):

    def post(self, request, *args, **kwargs):
        return JsonResponse({"instance": 'success'}, status=200)





