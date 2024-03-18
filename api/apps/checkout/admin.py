from django.contrib import admin
from .models import Address, Checkout, CheckoutItems

admin.site.register(Address)
admin.site.register(Checkout)
admin.site.register(CheckoutItems)

