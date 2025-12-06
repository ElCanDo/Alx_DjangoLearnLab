# Authentication System Documentation

This document explains the authentication system used in the `django_blog` project.  
It includes registration, login, logout, and profile functionality.

---

## 1. Registration
Files:
- `blog/forms.py`
- `blog/views.py`
- `blog/templates/blog/register.html`

The registration page allows users to:
- Create an account
- Enter username, email, password

Uses a custom form extending `UserCreationForm`.

---

## 2. Login
Files:
- `blog/views.py`
- `blog/templates/blog/login.html`

Users log in using:
- Username
- Password

If authentication is successful, they are redirected to their profile.

---

## 3. Logout
Files:
- `blog/views.py`

Logs the user out and redirects them to the login page.

---

## 4. Profile Page
Files:
- `blog/views.py`
- `blog/templates/blog/profile.html`

Features:
- Only accessible when logged in
- Shows user's username and email

Protected with `@login_required`.

---

## 5. URL Routing
Located in:
- `blog/urls.py`
- `django_blog/urls.py`

Routes:
/login
/logout
/register
/profile


---

## 6. Security
- All forms use CSRF protection
- Passwords are securely hashed by Django
- Profile and logout require the user to be logged in

---

## 7. Testing Instructions
### Registration
1. Visit `/register`
2. Fill the form
3. Submit → Redirects to login

### Login
1. Visit `/login`
2. Enter credentials
3. Redirects to `/profile`

### Logout
1. Click logout button
2. Should redirect to login

### Profile
1. Open `/profile` when logged in → Works
2. Try when logged out → Redirects to login

---

## 8. Summary
The authentication system provides:
- User registration
- Login and logout
- Protected profile page
- Secure handling of passwords and forms

It forms the core of user management for the blog project.