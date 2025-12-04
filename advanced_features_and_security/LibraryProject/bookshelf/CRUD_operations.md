# THE CREATE OPERATION

```python
#Create and add new book to add to bookshelf
Book.objects.create(
    title="1984", 
    author="George Orwell", 
    publication_year=1949
    )
```
---
# THE RETRIEVE OPRATION

```python
#List all available books in bookshelf
book_available = Book.objects.get(title="1984")
print(f"{self.title} by {self.author}, published in {self.publication_year}")
```
---
# THE UPDATE OPERATION

```Python
# Find the book you want to update
update = Book.objects.get(title="1984")
book.title = "Nineteen Eigthy-Four"
update.save() 
#Updates the title from "1984" to "Nineteen Eighty-Four"
```
---
# THE DELETE OPERATION

```Python
from bookshelf.models import Book

delete_book = Book.objects.get(title="Nineteen Eighty-Four")
delete_book.delete()
```