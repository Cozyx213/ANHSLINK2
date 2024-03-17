from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    grade = models.IntegerField(null=True)
    section = models.CharField(default='Selene', max_length=20)
    email = models.EmailField(default="haha@gmail.com")
    def __str__(self):
        return self.user.username
    