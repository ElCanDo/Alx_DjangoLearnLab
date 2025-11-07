from django.urls import path
from .views import list_books
from . views import LibraryDetailView

urlpatterns[
    # path('', views.index, name='index'),
    path('books/', list_books, name='book_list'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
]