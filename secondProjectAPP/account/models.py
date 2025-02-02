from django.db import models

# Create your models here.
class Account(models.Model):
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # Override the __str__ method to return a more useful string
    def __str__(self):
        return f"Account(id={self.id}, email={self.email}, username={self.username}, create_at ={self.create_at})"
