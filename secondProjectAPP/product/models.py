from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(max_length=100)
    product_name = models.TextField(max_length=255)
    product_price = models.IntegerField(max_length=100)
    product_type = models.TextField(max_length=255)
    product_date =models.DateTimeField(auto_now=True)
    product_weight = models.IntegerField(max_length=100)
    

# class cart(models.model):
#     user = 