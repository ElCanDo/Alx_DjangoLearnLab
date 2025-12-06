# Import forms module from Django
from django import forms
# Import built-in user creation form
from django.contrib.auth.forms import UserCreationForm
# Import the User model
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget
# Custom registration form extending Django's UserCreationForm
class RegisterForm(UserCreationForm):  
    email = forms.EmailField(required=True) # Add email field as a required field

    # Configure the form's metadata
    class Meta:
        # Specify the model to use
        model = User
        # Define the fields to display in the form
        fields = ["username", "email", "password1", "password2"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]  # Fields to include in the form


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]  # Field to include in the form
        widgets = {
            "tags": TagWidget(),  # Use TagWidget for tags field
        }