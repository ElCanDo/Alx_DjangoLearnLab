from rest_framework import serializers
from .models import Book, Author
from django.utils import timezone

# Serialization classes to handle Book and Author serialization
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Book #References Book model in models.py
        fields = '__all__' # Include all the fields in the Book instance

    #Custom validation for publication_year
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author # References the Author model in models.py
        fields = ['name'] # Include only the name field in the Author instance