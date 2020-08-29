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
    url('', include('libraries.urls'))


]
