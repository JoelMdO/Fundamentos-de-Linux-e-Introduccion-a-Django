from typing import Any
from django.db import models
from ecommerce.validators import validate_for_blocker_words
from base.models import BasePublishModel
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class ProductModel(BasePublishModel):
    
    title = models.TextField()
    price = models.FloatField()
    description = models.TextField(default="No description provided.")
    seller = models.CharField(max_length=100, default="Unknown Seller")
    color = models.CharField(max_length=50, default="black")
    product_dimensions = models.CharField(max_length=20, default="Not specified")
    slug = models.SlugField(unique=True, blank=True, db_index=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="products") #CASCADE deletes all the products of the user, SET_NULL does not

    def get_absolute_url(self) -> str:
        return f"/products/{self.slug}/"
    
    def save(self, *args: Any, **kwargs: Any) -> None:
        validate_for_blocker_words(self.title)
        super().save(*args, **kwargs)

    def is_published(self) -> bool:
        return self.state == "PB"
    
def slugify_pre_save(sender: type[ProductModel], instance: ProductModel, *args: Any, **kwargs: Any) -> None:
    if instance.slug == "":
        new_slug = slugify(instance.title)
        MyModel = instance.__class__
        qs = MyModel.objects.filter(slug__startswith=new_slug).exclude(pk=instance.pk)
        if qs.count() == 0:
            instance.slug = new_slug
        else:
            instance.slug = f"{new_slug}-{qs.count() + 1}"
pre_save.connect(slugify_pre_save, sender=ProductModel)

   