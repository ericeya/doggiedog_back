from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=300, unique=True)
    password = models.CharField(max_length=200)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
class Image(models.Model):
    imageSignedUrl = models.CharField(max_length=1000, default=None, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    uploaded_date = models.DateTimeField(auto_now_add=True, null=True)
    caption = models.TextField(default=None)

    def __str__(self): 
        return self.imageSignedUrl


