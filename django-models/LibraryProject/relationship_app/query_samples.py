from django.db import models

# List all books available in a Library.
books = Library.objects.get(name="books.all()")

# Filter by a specific author
books_by_author = Book.objects.filter(author)

# Query by 