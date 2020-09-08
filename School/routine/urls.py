from django.urls import path
from . import views

app_name = 'leave'

urlpatterns = [
    # type
    path('routines/', views.RoutineListView.as_view(), name="routines"),
]