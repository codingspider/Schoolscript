from django.urls import path

from . import views


urlpatterns = [
    path('join-friend', views.JoinFormView.as_view()),

]
