from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True)
    #avatar = models.ImageField(upload_to='avatars/', default='avatar.png')
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}--{self.created}"
