from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

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

class SignUpView(CreateView):
    """Handles user Signup using Django's built-in UserCreationForm."""
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def register(request):
    """Handles user registration using Django's built-in UserCreationForm."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Successful Registration! You can log in now.")
            return redirect(reverse_lazy('login'))
        else:
            form = UserCreationForm()
            return render(request, 'relationship_app/register.html', {'form':form})
    

class LogoutView(LogoutView):
    next_page = reverse_lazy('login')
    template_name = 'relationship_app/logout.html'

# def is_admin(user):
#     return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# def is_librarian(user):
#     return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# def is_member(user):
#     return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')

def user_role(role):
    def check(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return check

@user_passes_test(user_role('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(user_role('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(user_role('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Permission Required Decorator
@permission_required('relationship_app.can_add_book')
def add_book_view(request):
    # logic to add a book

@permission_required('relationship_app.can_change_book')
def add_book_view(request):
    # logic to add a book

@permission_required('relationship_app.can_delete_book')
def add_book_view(request):
    # logic to add a book
