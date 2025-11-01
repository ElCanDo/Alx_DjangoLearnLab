# THE DELETE OPERATION

```Python
from bookshelf.models import Book

delete_book = Book.objects.get(title="Nineteen Eighty-Four")
delete_book.delete()
```