from django.db import models

# List all books available.
books = Book.objects.all()

# Filter by a specific author
books_by_author = Book.objects.filter(author)

# Query by 