from django.contrib import admin
from .models import Address, Checkout, Payment, PaymentOptions, CheckoutItems

admin.site.register(Address)
admin.site.register(Checkout)
admin.site.register(Payment)
admin.site.register(PaymentOptions)
admin.site.register(CheckoutItems)
