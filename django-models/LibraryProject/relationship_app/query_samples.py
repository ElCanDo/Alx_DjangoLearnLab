from django.db import models

# List all books available in a Library.
Library = Library.objects.get(name='library_name')
books = library.books.all()

# Filter by a specific author
books_by_author = Book.objects.filter(name="author_name")

# Query by 