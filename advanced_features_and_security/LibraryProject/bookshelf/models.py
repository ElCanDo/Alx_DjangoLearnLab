from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.publication_year}"

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.username
    

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user
        
     
    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_staff = True 
        user.is_superuser = True
        user.save(using=self._db)

        
        

        permissions = Permission.objects.filter(codename__in=['can_view', 'can_create', 'can_edit', 'can_delete'])
        user.user_permissions.add(*permissions)

        return user
