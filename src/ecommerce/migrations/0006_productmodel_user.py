from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0005_productmodel_slug"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="productmodel",
            name="user",
            field=models.ForeignKey(
                to=settings.AUTH_USER_MODEL,
                null=True,
                on_delete=models.CASCADE,
                related_name="products",
            ),
        ),
    ]
