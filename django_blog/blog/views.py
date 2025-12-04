from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm # type: ignore
from django.contrib import messages

    # Handle user registration
def login_view(request):
    # Check if form was submittedest.POST)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # Validate form 
        if form.is_valid():
            user = form.save()  # Save new user to database
            messages.success(request, "Account created successfully!")
            return redirect("login")  # Redirect to login page
    else:
        # Display empty form for GET requests
        form = RegisterForm()
    return render(request, "blog/static/register.html", {"form": form}) 

# Handle user login
def login_view(request):
    if request.method == "POST":
        # Get username and password from form
        username = request.POST.get("username")      
        password = request.POST.get("password")

        # Check if credentials are correct
        user = authenticate(request, username=username, password=password)
        if user:    
            login(request, user)  # Log user in
            return redirect("profile")  # Go to profile page
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "blog/static/login.html")

# Handle user logout@login_required
def logout_view(request):
    logout(request)  # Clear user session 
    return redirect("login")  # Go back to login page

# Show user profile (only for logged-in users)
@login_required
def profile_view(request):
    return render(request, "blog/static/profile.html", {"user": request.user})
