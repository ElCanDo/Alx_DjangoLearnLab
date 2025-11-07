from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Book

# Create your views here.
def book_list(request):
    books = Book.objects.all() #Fetch all books from database
    context = {'book_list': books} #Creates a context dictionary with book list
    return render(request, 'list_books.html', context)

class LibraryDetailView(TemplateView):
    template_name = 'library_detail.html'