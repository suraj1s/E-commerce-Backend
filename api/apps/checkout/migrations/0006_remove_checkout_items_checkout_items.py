# Generated by Django 5.0.1 on 2024-03-17 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_status'),
        ('checkout', '0005_alter_payment_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='items',
        ),
        migrations.AddField(
            model_name='checkout',
            name='items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
        ),
    ]
