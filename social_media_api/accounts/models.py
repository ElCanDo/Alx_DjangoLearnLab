from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField()
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followers_set')
    following = models.ManyToManyField('self', symmetrical=False, related_name='following_set')
