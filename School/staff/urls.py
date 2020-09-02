from django.urls import path
from . import views


urlpatterns = [

    path('professionals', views.StaffListView.as_view(), name="professionals-list"),
    path('add_professionals/', views.StaffAddView.as_view(), name="add_professionals"),
    path('professionals_add_parent/<int:pk>', views.StaffAddParentView.as_view(), name="professionals_add_parent"),
    path('add_family_information/', views.AddFamilyInformationView.as_view(), name="add_family_information"),
    path('delete_staff/', views.DeleteStaffView.as_view(), name='delete_staff'),
    path('edit_staff_information/<int:pk>', views.EditStaffInformation.as_view(), name="edit_staff_information"),
    path('update_staff_information/', views.UpdateStaffInformationView.as_view(), name="update_staff_information"),

]
