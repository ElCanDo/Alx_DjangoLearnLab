from django.urls import path
from .views import list_books
from . views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
urlpatterns[
    path('books/', list_books, name='book_list'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.registerView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), template_name='relationship/logout.html'),
    path('login/', LoginView.as_view(), template_name='relationship_app/login.html'),

]