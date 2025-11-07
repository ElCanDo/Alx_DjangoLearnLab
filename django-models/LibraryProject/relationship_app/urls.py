from django.urls import path
from .views import list_books
from . views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView, RegisterView

urlpatterns[
    # path('', views.index, name='index'),
    path('books/', list_books, name='book_list'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login.html'),
    path('logout/', LogoutView.as_view(), name='logout.html'),

]