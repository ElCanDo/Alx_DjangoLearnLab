# THE CREATE OPERATION

```python
#Create a new book to add to bookshelf
new_book = Book.object.create(
    title="1984", 
    author="George Orwell", 
    publication_year=1949
    )
new_book.save()  #Save new book created to bookshelf
```