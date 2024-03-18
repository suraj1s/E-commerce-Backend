from django.contrib import admin
from .models import Payment, PaymentOptions
# Register your models here.
admin.site.register(Payment)
admin.site.register(PaymentOptions)