from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Emailc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)