from django.urls import path
from . import views


urlpatterns = [

    path('professionals', views.StaffListView.as_view(), name="professionals-list"),
    path('add_professionals/', views.StaffAddView.as_view(), name="add_professionals"),
    path('professionals_add_parent/<int:pk>', views.StaffAddParentView.as_view(), name="professionals_add_parent"),
    path('add_family_information/', views.AddFamilyInformationView.as_view(), name="add_family_information")

]