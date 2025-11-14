from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from.models import CustomUser

class BookAdmin(admin.ModelAdmin):
    list_filter = ("title", "author", "publication_year")
    search_fields = ("title", "author")
# Register the Book model 
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)
