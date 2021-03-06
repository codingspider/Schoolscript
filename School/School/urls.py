from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from institute.models import *

from ajax.views import JoinFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('institute.urls')),
    path('', include('hostels.urls')),
    path('', include('crop.urls')),
    path('', include('parent.urls')),
    path('', include('student.urls')),
    path("select2/", include("django_select2.urls")),
    path('', include('teacher.urls')),
    path('', include('commitee.urls')),
    url(r'^join/', JoinFormView.as_view()),
    url('teste/', include('teste.urls')),
    url('', include('modelmanager.urls')),
    url('', include('libraries.urls')),
    url('', include('announcement.urls')),
    url('leave/', include('leave.urls')),
    url('', include('frontoffice.urls')),
    url('', include('transports.urls')),
    url('', include('staff.urls')),
    url('', include('subject.urls')),
    url('', include('exam.urls')),
    url('', include('attendence.urls')),
    url('', include('routine.urls')),
    url('', include('syllabus.urls')),


]
