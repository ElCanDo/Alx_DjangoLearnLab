from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

def list_books(request):
    ...
    books = Book.objects.all() #Fetch all books from database
    context = {'book_list': books} #Creates a context dictionary with book list
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """Show details of a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
def index(request):
    return render(request, 'relationship_app/index.html')

class RegisterView(CreateView):
    """Handles user registration using Django's built-in UserCreationForm."""
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"
    
def register(request):
    return RegisterView.as_view()(request)

class LogoutView(LogoutView):
    next_page = reverse_lazy('login')
    template_name = 'relationship_app/logout.html'
