from django.db import models
from api.apps.common.models import BaseModel
from api.apps.auth.models import CustomUser as User
from api.apps.cart.models import Cart

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


class PaymentMethodEnun(models.TextChoices):
    CREDIT_CARD = 'credit_card'
    DEBIT_CARD = 'debit_card'
    PAYPAL = 'paypal'
    STRIPE = 'stripe'
    CASH_ON_DELIVERY = 'cash_on_delivery'
    ESEWA = 'esewa'

class PaymentStatusEnun(models.TextChoices):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    FAILED = 'failed'
    
class Payment(BaseModel):
    payment_method = models.CharField(max_length=255, choices=PaymentMethodEnun.choices)
    payment_status = models.CharField(max_length=255, choices=PaymentStatusEnun.choices, default=PaymentStatusEnun.PENDING)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_reference = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE )


    def __str__(self):
        return f'{self.payment_method} - {self.payment_amount}'

class Checkout(BaseModel):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Cart, on_delete=models.CASCADE , default=None)
    def __str__(self):
        return f'{self.address} - {self.payment} - {self.user}'