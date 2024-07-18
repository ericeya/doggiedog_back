from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from storages.backends.s3boto3 import S3Boto3Storage

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=300, unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True, default=None)
    
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

class CustomS3Boto3Storage(S3Boto3Storage):
    def generate_filename(self, filename):
        ext = filename.split('.')[-1]
        new_filename = f"{uuid.uuid4().hex}.{ext}"
        return new_filename

class Image(models.Model):
    image = models.FileField(upload_to='images/', default=None, storage=CustomS3Boto3Storage())
    uploaded_date = models.DateTimeField(auto_now_add=True, null=True)
    caption = models.TextField(max_length=1000, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self): 
        return f"Image uploaded by {self.user.username} on {self.uploaded_date} with caption: {self.caption}"


