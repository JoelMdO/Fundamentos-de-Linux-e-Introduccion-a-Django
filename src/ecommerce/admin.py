from django.contrib import admin

# Register your models here.
from .models import ProductModel

admin.site.register(ProductModel)
