from django.urls import path
from .views import hostel_type, hostel, room_type, room, designation
from hostels.views import hostel_type
from hostels.views import hostel


urlpatterns = [
    #hostel type
    path('types', hostel_type.TypesListView.as_view(), name='types'),
    path('add_hostel_type/', hostel_type.AddHostelType.as_view(), name="add_hostel_type"),
    path('edit_hostel_type/<int:pk>', hostel_type.EditHostelTypeView.as_view(), name="edit_hostel_type"),
    path('update_hostel_type/', hostel_type.UpdateHostelTyepView.as_view(), name="update_hostel_type"),
    path('delete_hostel_type/', hostel_type.DeleteHostelTypeView.as_view(), name="delete_hostel_type"),
    
    #hostel
    path('hostels', hostel.HostelListView.as_view(), name='hostels'),
    path('add_hostel/', hostel.AddHostelView.as_view(), name="add_hostel"),
    path('hostel_detail/<int:pk>/', hostel.HostelDetailView.as_view(), name='hostel_detail'),
    path('edit_hostel/<int:pk>/', hostel.HostelEditView.as_view(), name='edit_hostel'),
    path('update_hostel/', hostel.HostelUpdateView.as_view(), name='update_hostel'),
    path('delete_hostel/', hostel.HostelDeleteView.as_view(), name='delete_hostel'),


    #Room Type Urls
    path('room_types', room_type.RoomTypeListView.as_view(), name="room_types"),
    path('add_room_type/', room_type.TypeCreateView.as_view(), name="add-room-type"),
    path('edit_room_type/<int:pk>', room_type.RoomTypeUpdateView.as_view(), name="edit_room_type"),
    path('delete_room_type/', room_type.RoomTypeDeleteView.as_view(), name="delete_room_type"),


    # room
    path('rooms/', room.RoomListView.as_view(), name="rooms"),
    path('add_room/', room.AddRoomView.as_view(), name="add-room"),
    path('edit_room/<int:pk>', room.RoomUpdateView.as_view(), name="edit_room"),
    path('update_room/', room.RoomUpdate.as_view(), name="update_room"),
    path('delete_room/', room.RoomDeleteView.as_view(), name="delete_room"),
    path('room/<int:pk>', hostel.HostelRoomView.as_view(), name="hostel_room"),
    path('add_hostel_room/', hostel.AddRoomViewHostel.as_view(), name="add_hostel_room"),
    path('add_hostel_room/<int:pk>', hostel.AddHostelRoomView.as_view(), name="add_hostel_room"),
    path('delete_room/<int:pk>/', hostel.DeleteHostelRoomView.as_view(), name="delete_room"),
    path('assign_student/<int:pk>/<int:room>', hostel.AddStudentView.as_view(), name="assign_student"),
    path('add_student_room', hostel.AssignStudentView.as_view(), name="add_student_room"),
    path('hostel_add_student/<int:pk>', hostel.DerectAddStudent.as_view(), name="hostel_add_student"),
    path('hostel_staff/<int:pk>', hostel.AddStaffView.as_view(), name="hostel_staff"),
    path('assign_staff', hostel.AssignStaff.as_view(), name="assign_staff"),


    # designation
    path('designations/', designation.IndexView.as_view(), name="designations"),
    path('add_designation/', designation.AddView.as_view(), name="add_designation"),
    path('edit_designation/<int:pk>', designation.DesignationUpdateView.as_view(), name="edit_designation"),
    path('update_designation/', designation.DesignationUpdate.as_view(), name="update-designation"),
    path('delete_designation/', designation.DesignationDeleteView.as_view(), name="delete-designation"),

]