from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters
from .models import Book
from .serializers import BookSerializer


# Create your views here.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticatedOrReadOnly, IsAuthenticated
    filter_backends = [ filters.SearchFilter, filters.OderingFilter]
    search_fields = []
    odering_fields = ['title', 'publication_year']

class DetailView(generics.RetrieveAPIView):
    queryset = Book.object.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticatedOrReadOnly, IsAuthenticated


class CreateView(generics.CreateAPIView):
    queryset = Book.object.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticatedOrReadOnly, IsAuthenticated



class UpdateView(generics.UpdateAPIView):
    queryset = Book.object.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticatedOrReadOnly, IsAuthenticated


class DeleteView(generics.DestroyAPIView):
    queryset = Book.object.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticatedOrReadOnly, IsAuthenticated
