from django.db import models

class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for prices
    product_type = models.CharField(max_length=255)
    product_date = models.DateTimeField(auto_now=True)
    product_weight = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for weight if it's a decimal

    def __str__(self):
        return f"Product(id={self.product_id}, name={self.product_name}, price={self.product_price}, type={self.product_type})"
