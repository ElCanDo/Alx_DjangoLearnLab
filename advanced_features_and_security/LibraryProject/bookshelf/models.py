from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission
from django.conf import settings


# Models and a custom user manager for the app.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        # Extra model permissions beyond Django's defaults.
        permissions = [
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.publication_year}"


class CustomUser(AbstractUser):
    # Extra profile fields.
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    # Manager is assigned after CustomUserManager is defined.
    objects = BaseUserManager()

    def __str__(self):
        return self.username


class CustomUserManager(BaseUserManager):
    """Manager providing create_user and create_superuser helpers."""

    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("The username must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not password:
            raise ValueError("Superusers must have a password.")

        user = self.create_user(username, email, password, **extra_fields)

        # Optionally add specific permissions to the superuser.
        try:
            permissions = Permission.objects.filter(
                content_type__app_label='bookshelf',
                codename__in=['can_create', 'can_edit', 'can_delete_book', 'view_book']
            )
            user.user_permissions.add(*permissions)
        except Exception:
            # Ignore permission assignment errors (e.g., permissions not yet created).
            pass

        return user


# Attach the custom manager to CustomUser now that it's defined.
CustomUser.add_to_class('objects', CustomUserManager())

# Use settings.AUTH_USER_MODEL when referencing the user model in relations.
# Example (inside another model):
# user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
