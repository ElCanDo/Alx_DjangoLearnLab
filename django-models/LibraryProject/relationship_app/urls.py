from django.urls import path
from .views import list_books
from . views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from .import views
urlpatterns=[
    path('books/', list_books, name='book_list'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', name='add_book'),
    path('edit_book/', name='edit_book'),
    path('delete_book/', name='delete_book')

]
auth_patterns=[
    #Registration
    path('register/', views.register(template_name='relationship_app/register.htm'), name='register'),
    #Logout
    path('logout/', LogoutView.as_view(template_name='relationship/logout.html'), name='logout'),
    #Login
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

] + urlpatterns