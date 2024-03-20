# Generated by Django 5.0.1 on 2024-03-20 16:12

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentOptions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_method', models.CharField(max_length=255)),
                ('payment_description', models.TextField()),
                ('payment_type', models.CharField(choices=[('credit card', 'Credit Card'), ('debit card', 'Debit Card'), ('paypal', 'Paypal'), ('cash on delivery', 'Cash On Delivery'), ('bank transfer', 'Bank Transfer'), ('bitcoin', 'Bitcoin'), ('other', 'Other')], default='other', max_length=255)),
                ('payment_image', models.ImageField(blank=True, null=True, upload_to='media/payment_options/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('failed', 'Failed'), ('hold', 'Hold')], default='pending', max_length=255)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_reference', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.paymentoptions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
