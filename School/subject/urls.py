from django.urls import path
from . import views


urlpatterns = [
    #subject
    path('subjects', views.SubjectListView.as_view(), name="subjects"),
    path('add_subject/', views.SubjectAddView.as_view(), name="add_subject"),
    path('edit_subject/<int:pk>', views.SubjectEditView.as_view(), name="edit_subject"),
    path('update_subject/', views.SubjectUpdateView.as_view(), name="update_subject"),
    path('delete_subject/', views.SubjectDeleteView.as_view(), name="delete_subject"),

]