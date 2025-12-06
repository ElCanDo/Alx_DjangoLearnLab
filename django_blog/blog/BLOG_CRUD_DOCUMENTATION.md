# Blog CRUD Documentation

This document explains how the CRUD (Create, Read, Update, Delete) system for blog posts works in the `django_blog` project.

---

## 1. Post Model
Located in: `blog/models.py`

The Post model stores:
- title
- content
- author (User)
- created_at (timestamp)

---

## 2. Forms
Located in: `blog/forms.py`

A `PostForm` is created using Django’s `ModelForm`.  
It includes:
- title
- content

The author is set automatically in the view.

---

## 3. CRUD Views
Located in: `blog/views.py`

### List Posts
- Shows all posts.
- Accessible to everyone.

### View Post Detail
- Shows a single post.

### Create Post
- Only for logged-in users.
- Author is assigned automatically.

### Edit Post
- Only the author can edit.

### Delete Post
- Only the author can delete.

Used Mixins:
- `LoginRequiredMixin`
- `UserPassesTestMixin`

---

## 4. URL Patterns
Located in: `blog/urls.py`

/ → List all posts
/posts/<pk>/ → View a single post
/posts/new/ → Create a new post
/posts/<pk>/edit/ → Edit a post
/posts/<pk>/delete/ → Delete a post


---

## 5. Templates
Stored in: `blog/templates/blog/`

Templates include:
- `post_list.html`
- `post_detail.html`
- `post_form.html` (used for create + edit)
- `post_confirm_delete.html`

---

## 6. Permissions
- Anyone can read posts.
- Only authenticated users can create posts.
- Only the author can edit or delete a post.

---

## 7. Testing Instructions
- Create several posts while logged in.
- Try editing/deleting your posts → Success.
- Attempt editing/deleting another user’s post → Should block access.
- Visit list and detail pages without logging in → Should work.

---

## 8. Summary
The CRUD system allows users to:
- View blog posts
- Create new posts
- Edit their own posts
- Delete their own posts

Everything else is protected to maintain security and ownership.