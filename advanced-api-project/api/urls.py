from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('books/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailView.as_view(), name='retrieve-book-detail'),
    path('books/', CreateView.as_view(), name='add-new-book'),
    path('books/<int:pk>/', UpdateView.as_view(), name='modify-existing-book'),
    path('books/<int:pk>/', DeleteView.as_view(), name='remove-book'),
]