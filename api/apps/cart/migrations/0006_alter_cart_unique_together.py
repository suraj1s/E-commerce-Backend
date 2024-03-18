# Generated by Django 5.0.1 on 2024-03-18 03:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_cart_unique_together'),
        ('product', '0011_rename_thumbnail_url_product_thumbnail'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'product')},
        ),
    ]
