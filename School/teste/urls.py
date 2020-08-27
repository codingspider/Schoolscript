from django.urls import path

from . import views

app_name = "teste"

urlpatterns = [
    path('add_institute/', views.AddInstituteView.as_view(), name= "add_institute"),
]

