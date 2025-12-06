# Import forms module from Django
from django import forms
# Import built-in user creation form
from django.contrib.auth.forms import UserCreationForm
# Import the User model
from django.contrib.auth.models import User

# Custom registration form extending Django's UserCreationForm
class RegisterForm(UserCreationForm):  
    email = forms.EmailField(required=True) # Add email field as a required field

    # Configure the form's metadata
    class Meta:
        # Specify the model to use
        model = User
        # Define the fields to display in the form
        fields = ["username", "email", "password1", "password2"]