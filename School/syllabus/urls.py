from django.urls import path
from . import views

app_name = 'syllabus'

urlpatterns = [
    # type
    path('syllabus', views.SyllabusListView.as_view(), name="syllabus"),
    path('add_syllabus/', views.SyllabusAddView.as_view(), name="add_syllabus"),
    path('edit_syllabus/<int:pk>', views.SyllabusEditView.as_view(), name="edit_syllabus"),
    path('update_syllabus/', views.SyllabusUpdateView.as_view(), name="update_syllabus"),
    path('delete_syllabus/', views.SyllabusDeleteView.as_view(), name="delete_syllabus"),
]