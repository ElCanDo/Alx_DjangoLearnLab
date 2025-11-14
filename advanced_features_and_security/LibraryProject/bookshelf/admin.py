from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    list_filter = ("title", "author", "publication_year")
    search_fields = ("title", "author")
# Register the Book model 
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    #Visible fields when viewing a user
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields':('date_of_birth', 'profile_photo')}),
                                     )
    #Visible fields when creating a user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo'),})
    )
admin.site.register(CustomUser, CustomUserAdmin)
