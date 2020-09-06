from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('attendences', views.AttendenceListView, name='attendence_list'),
    path('get_student_list_for_attendance/', views.StudentListView.as_view(), name='list_for_attendance'),
    path('attendance_save_attendance/', views.AttendanceSaveView.as_view(), name='save_attendance'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
