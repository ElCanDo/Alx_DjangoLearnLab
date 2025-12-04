from .models import Author, Library, Librarian

# List all books available in a Library.
Library = Library.objects.get(name='library_name')
books = Library.books.all()

# Filter by a specific author
list_author = Author.objects.get(name='author_name')
books_by_author = Author.objects.filter(author='author')

#Retrieve Librarian for a library
Librarian = Librarian.objects.get(library='library')