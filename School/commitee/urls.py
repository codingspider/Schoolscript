from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('committees', views.CommiteeListView.as_view(), name="committees"),
    path('add_committee', views.CommiteeAddView.as_view(), name="add_committee"),
    path('committee_detail/<int:pk>', views.CommiteeDetailView.as_view(), name="committee_detail"),
    path('edit_committee/<int:pk>', views.CommiteeUpdateView.as_view(), name="edit_committee"),
    path('delete_committee/<int:pk>', views.CommiteeDeleteView.as_view(), name="delete_committee"),


]