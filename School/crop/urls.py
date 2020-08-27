from django.conf import settings
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url('crop/image', views.photo_list, name='photo_list'),
    path('crud/', views.CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/', views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/update/', views.UpdateCrudUser.as_view(), name='crud_ajax_update'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)