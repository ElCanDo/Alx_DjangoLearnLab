from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    display_list = ("title", "author", "publication_year")
# Register the Book model 
admin.site.register(Book, BookAdmin)
