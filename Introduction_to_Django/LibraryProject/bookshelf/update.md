# THE UPDATE OPERATION

```Python
# Find the book you want to update
update = Book.objects.get(title="1984")
self.title = "Nineteen Eigthy-Four"
update.save() 
#Updates the title from "1984" to "Nineteen Eighty-Four"