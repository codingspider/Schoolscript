from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    # Exam
    path('exam-list-view/', views.ExamListView.as_view(), name="exam-list"),
    path('add_exam/', views.ExamAddView.as_view(), name="add_exam"),
    path('edit_exam/<int:pk>', views.ExamEditView.as_view(), name="edit_exam"),
    path('update_exam/', views.ExamEditView.as_view(), name="update_exam"),
    path('delete_exam/', views.ExamDeleteView.as_view(), name="delete_exam"),
    path('delete_result/', views.ResultDeleteView.as_view(), name="delete_result"),

    #mark
    path('exam_marks/', views.ExamMarksListView.as_view(), name="exam_marks_list"),
    path('get_all_student', views.ExamGetStudentView.as_view(), name="get_all_student"),
    path('add_marks_to_student', views.AddExamMarkView.as_view(), name="add_mark"),


]