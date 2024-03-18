
from django.db import models
from api.apps.common.models import BaseModel
from api.apps.auth.models import CustomUser as User
from api.apps.cart.models import Cart
from api.apps.product.models import Product
from api.apps.payment.models import  Payment


class Address(BaseModel):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    street_address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE )

    def __str__(self):
        return f'{self.city}, {self.state}, {self.country}'


class CheckoutItems (BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product} - {self.quantity}'

class Checkout(BaseModel):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout_items = models.ManyToManyField(CheckoutItems)
    def __str__(self):
        return f'{self.user} - {self.payment} - {self.address}'


