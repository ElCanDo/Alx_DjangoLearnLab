from django.urls import path
from .views import list_books
from . views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
urlpatterns=[
    path('books/', list_books, name='book_list'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
]
auth_patterns=[
    #Registration
    path('register/', views.Register(template_name='relationship_app/register.htm'), name='register'),
    #Logout
    path('logout/', LogoutView.as_view(template_name='relationship/logout.html'), name='logout'),
    #Login
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

] + urlpatterns