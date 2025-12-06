from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm # type: ignore
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from . models import Post, Comment
from . forms import PostForm, CommentForm
    # Handle user registration
def register_view(request):
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
    return render(request, "blog/register.html", {"form": form}) 


# Handle user login
def login_view(request):
    if request.method == "POST":
        # Get username and password from form
        username = request.POST.get("username")      
        password = request.POST.get("password")

        # Check if credentials are correct
        user = authenticate(request, username=username, password=password)
        
        if user is not None:    
            login(request, user)  # Log user in
            return redirect("profile")  # Go to profile page
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "blog/login.html")


# Handle user logout@login_required
def logout_view(request):
    logout(request)  # Clear user session 
    return redirect("login")  # Go back to login page


# Show user profile (only for logged-in users)
@login_required
def profile_view(request):
    return render(request, "blog/profile.html", {"user": request.user})

"""CRUD Operations For Blog Posts"""

# View to list all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

# View to show details of a single blog post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

 # View to create a new blog post   
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template = 'blog/post_form.html'

# View to update an existing blog post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template = 'blog/post_form.html'

    # Ensure only the author can update the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# View to delete a blog post
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")  # Redirect to post list after deletion
    template_name = 'blog/post_confirm_delete.html'

    # Ensure only the author can delete the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

"""CRUD Operations For Comments"""
class PostListView(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'
    ordering = ['-created_at']

# View to create a new comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    
    # Set the author and associated post before saving the comment
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        return super().form_valid(form)

# View to update an existing comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    # Ensure only the author can update the comment
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

# View to delete a comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_confirm_delete.html'
  