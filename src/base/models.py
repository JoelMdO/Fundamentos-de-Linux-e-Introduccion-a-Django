from django.db import models
from django.utils import timezone
from typing import Any


# Create your models here.
class BasePublishModel(models.Model):
    class ProductStateOptions(models.TextChoices):
        PUBLISHED = "PB", "Published"
        DRAFT = "DR", "Draft"
        BROKEN = "BR", "Broken"

    state = models.CharField(max_length=2,  choices=ProductStateOptions.choices, default=ProductStateOptions.DRAFT)
    timestamp = models.DateTimeField(auto_now_add=True,)
    updated = models.DateTimeField(auto_now=True, null=True)
    publish_timestamp = models.DateTimeField(null=True)

    class Meta:
        abstract = True
        ordering = ['-publish_timestamp', '-updated', '-timestamp']
    def save(self, *args: Any, **kwargs: Any) -> None:
        if self.state_is_published and self.publish_timestamp is None:
            self.publish_timestamp = timezone.now()
        else:
            self.publish_timestamp = None
        super().save(*args, **kwargs)

    @property
    def state_is_published(self) -> bool:
        return self.state == self.ProductStateOptions.PUBLISHED.value

    def is_published(self) -> bool:
        publish_timestamp = self.publish_timestamp or self.timestamp
        return self.state_is_published and publish_timestamp < timezone.now()