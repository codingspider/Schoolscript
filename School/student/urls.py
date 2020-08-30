from django.urls import path

from . import views


urlpatterns = [
    path('students', views.StudentListView.as_view(), name='students'),
    path('add_student/', views.StudentAddView.as_view(), name='add_student'),
    path('student_details/<int:pk>', views.StudentDetailsView.as_view(), name='student_details'),
    path('edit_student/<int:pk>', views.StudentEditView.as_view(), name='edit_student'),
    path('update_student/', views.StudentUpdateView.as_view(), name='update_student'),
    path('delete_student/', views.StudentDeleteView.as_view(), name='delete_student'),


]