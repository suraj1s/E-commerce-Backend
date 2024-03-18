from django.contrib import admin
from .models import Address, Checkout, Payment, PaymentOptions

admin.site.register(Address)
admin.site.register(Checkout)
admin.site.register(Payment)
admin.site.register(PaymentOptions)

