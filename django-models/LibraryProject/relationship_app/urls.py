from django.urls import path
from .views import list_books
from . views import LibraryDetailView
from django.contrib.auth.views import LoginView, logoutView

urlpatterns[
    # path('', views.index, name='index'),
    path('books/', list_books, name='book_list'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logoutView.as_view(), name='logout'),
]