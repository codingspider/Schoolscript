from django.urls import path

from . import views


urlpatterns = [
    path('parents', views.ParentListView.as_view(), name='parent-list'),
    path('add_parent', views.ParentAddView.as_view(), name='parent-add'),
    path('edit_parent/<int:pk>', views.ParentEditView.as_view(), name='edit_parent'),
    path('update_parent/', views.ParentUpdateView.as_view(), name='update_parent'),
    path('detail_parent/<int:pk>', views.ParentDetailView.as_view(), name='detail_parent'),
    path('delete_parent/<int:pk>', views.DeleteParentView.as_view(), name='delete_parent'),
]