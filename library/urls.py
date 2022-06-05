from django.urls import path
from library import views

urlpatterns = [
    path("stdlist/",views.student_list_view),
    path("stddetail/<int:id>/",views.student_detail_view),
    path("booklist/",views.book_list_view),
    path("bookdetail/<int:id>/",views.book_detail_view),
    path("stdadd/",views.student_add_view),
    path("bookadd/",views.book_add_view),
    path("update/<int:id>/",views.student_update_view),
    path("stddelete/<int:id>/",views.student_delete_view),
    path("bookdelete/<int:id>/",views.book_delete_view),
    path("register/",views.admin_register_view),








]