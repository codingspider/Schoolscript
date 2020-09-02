from django.urls import path
from . import views

urlpatterns = [

    #Author
    path('author_list', views.AuthorListView.as_view(), name="authors"),
    path('add_author/', views.AuthorCreateView.as_view(), name="add_author"),
    path('edit_author/<int:pk>', views.AuthorEditView.as_view(), name="edit_author"),
    path('update_author/', views.AuthorUpdateView.as_view(), name="update_author"),
    path('delete_author/', views.AuthorDeleteView.as_view(), name="delete_author"),
    
    #publisher
    path('publisher_list/', views.PublisherListView.as_view(), name="publishers"),
    path('add_publisher/', views.PublisherAddView.as_view(), name="add_publisher"),
    path('edit_publisher/<int:pk>', views.PublisherEditView.as_view(), name="edit_publisher"),
    path('update_publisher/', views.PublisherUpdateView.as_view(), name="update_publisher"),
    path('delete_publisher/', views.PublisherDeleteView.as_view(), name="delete_publisher"),
    
    #subject
    # path('subjects', views.SubjectListView.as_view(), name="subjects"),
    # path('add_subject/', views.SubjectAddView.as_view(), name="add_subject"),
    # path('edit_subject/<int:pk>', views.SubjectEditView.as_view(), name="edit_subject"),
    # path('update_subject/', views.SubjectUpdateView.as_view(), name="update_subject"),
    # path('delete_subject/', views.SubjectDeleteView.as_view(), name="delete_subject"),

    #book_language
    path('book_language_list/', views.BookLanguageListView.as_view(), name="book_language_list"),
    path('add_book_language/', views.BookLanguageAddView.as_view(), name="add_book_language"),
    path('book_language_edit/<int:pk>', views.BookLanguageEditView.as_view(), name="book_language_edit"),
    path('update_book_language/', views.BookLanguageUpdateView.as_view(), name="update_book_language"),
    path('book_language_delete/', views.BookLanguageDeleteView.as_view(), name="book_language_delete"),

    #rack
    path('rack_list/', views.RackListView.as_view(), name="rack_list"),
    path('add_rack/', views.RackAddView.as_view(), name="add_rack"),
    path('edit_rack/<int:pk>', views.RoomEditView.as_view(), name="edit_rack"),
    path('update_rack/', views.RoomUpdateView.as_view(), name="update_rack"),
    path('delete_rack/', views.RackDeleteView.as_view(), name="delete_rack"),

    #book
    path('book_list/', views.BookListView.as_view(), name="book_list"),
    path('detail_book/<int:pk>', views.BookDetailView.as_view(), name="detail_book"),
    path('add_book/', views.BookAddView.as_view(), name="add_book"),
    path('edit_book/<int:pk>', views.BookEditView.as_view(), name="edit_book"),
    path('update_book/', views.BookUpdateView.as_view(), name="update_book"),
    path('book_delete/', views.BookDeleteView.as_view(), name="book_delete"),
    
    
    #ebook
    path('ebook_list', views.EbookListView.as_view(), name="ebook_list"),
    path('ebook/view/<int:pk>', views.ebook_view, name="ebook.view"),
    path('add_ebook/', views.AddEbookView.as_view(), name="add_ebook"),
    path('edit_ebook/<int:pk>', views.EbookEditView.as_view(), name="edit_ebook"),
    path('update_ebook/', views.EbookUpdateView.as_view(), name="update_ebook"),
    path('delete_ebook/', views.EbookDeleteView.as_view(), name="delete_ebook"),


    #book_issue
    path('book_issue_list/', views.book_issue, name="book_issue.list"),
    path('book_return_list', views.book_return, name="book_return_list"),
    path('book_issue_view/<int:pk>', views.book_issue_view, name="book_issue_view"),
    path('book_issue_create/<int:pk>', views.book_issue_create, name="book_issue_create"),
    path('book_issue_edit/<int:pk>/<int:book>', views.BookIssueEditView.as_view(), name="book_issue_edit"),
    path('book_issue_update/', views.BookIssueUpdateView.as_view(), name="book_issue_update"),
    path('book_issue_delete/', views.BookIssueDeleteView.as_view(), name="book_issue_delete"),
    path('make_return/<int:pk>', views.make_return, name="make_return"),
    
]
