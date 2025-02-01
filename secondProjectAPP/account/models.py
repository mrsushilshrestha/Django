from django.db import models

# Create your models here.
class Account(models.Model):
    email= models.EmailField(max_length=100)
    username =models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
