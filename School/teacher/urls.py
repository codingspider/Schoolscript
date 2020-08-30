from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('teachers', views.TeacherListView.as_view(), name="teachers"),
    path('add_teacher/', views.TeacherAddView.as_view(), name="add_teacher"),
    path('teacher_detail/<int:pk>', views.TeacherDetailView.as_view(), name="teacher_detail"),
    path('edit_teacher/<int:pk>', views.TeacherEditView.as_view(), name="edit_teacher"),
    path('update_teacher/', views.TeacherUpdateView.as_view(), name="update_teacher"),
    path('delete_teacher/', views.TeacherDeleteView.as_view(), name="delete_teacher"),


]