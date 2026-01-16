from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class DigitalProduct(Product):
   class Meta:
         proxy = True
         ## Muestra modelos diferentes en el admin pero 
         ## no crea una tabla nueva en la base de datos 
         ## por ejemplo difiriendo la forma de entrega, donde
         ## los productos digitales no requieren envío físico

