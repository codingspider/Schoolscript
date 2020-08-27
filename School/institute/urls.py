from django.urls import path

from . import views

app_name = "institute"
urlpatterns = [
    path('institutes', views.AllInstituteView.as_view(), name='institutes'),
    path('ajax/load-state/', views.load_state, name='ajax_load_state'),
    path('ajax/load-city/', views.load_cities, name='ajax_load_city'),
    path('institute_detail/<int:pk>', views.InstituteDetailView.as_view(), name='institute_detail'),
    path('edit_institute_view/<int:pk>/', views.InstituteEditView.as_view(), name='edit_institute_view'),
    path('delete_institute/',  views.InstituteDeleteView.as_view(), name='crud_ajax_delete'),
    path('add_institute/', views.AddInstituteView.as_view(), name="add_institute"),
    path('edit_institute/', views.EditInstituteView.as_view(), name="edit_institute"),
    path('edit_institute_image/', views.InstituteImageEdit.as_view(), name="edit_institute_image"),

]

