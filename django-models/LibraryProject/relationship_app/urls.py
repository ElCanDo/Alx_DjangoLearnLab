from django.urls import path
from .views import list_books
from . views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
urlpatterns=[
    path('books/', list_books, name='book_list'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

]
auth_patterns=[
    #Registration
    path('register/', views.register(template_name='relationship_app/register.htm'), name='register'),
    #Logout
    path('logout/', LogoutView.as_view(template_name='relationship/logout.html'), name='logout'),
    #Login
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

] + urlpatterns