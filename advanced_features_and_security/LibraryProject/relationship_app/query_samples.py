from relationship_app.models import models

# List all books available in a Library.
Library = Library.objects.get(name=library_name)
books = library.books.all()

# Filter by a specific author
list_author = Author.objects.get(name=author_name)
books_by_author = Author.objects.filter(author=author)

#Retrieve Librarian for a library
Librarian = Librarian.objects.get(library=library)