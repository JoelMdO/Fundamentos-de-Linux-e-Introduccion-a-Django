from django.db import models

# Create your models here.
class ProductModel(models.Model):
    title = models.TextField()
    price = models.FloatField()
    description = models.TextField(default="No description provided.")
    seller = models.CharField(max_length=100, default="Unknown Seller")
    color = models.CharField(max_length=50, default="black")
    product_dimensions = models.CharField(max_length=20, default="Not specified")
    # name = models.CharField(max_length=100)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
 

    # def __str__(self):
    #     return self.title