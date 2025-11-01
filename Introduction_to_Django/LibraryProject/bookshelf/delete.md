# THE DELETE OPERATION

```Python
delete_book = Book.objects.get(title="Nineteen Eighty-Four")
delete_book.delete()