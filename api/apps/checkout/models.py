
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

class PaymentTypeEnun(models.TextChoices):
    CREDIT_CARD = 'credit card'
    DEBIT_CARD = 'debit card'
    PAYPAL = 'paypal'
    CASH_ON_DELIVERY = 'cash on delivery'
    BANK_TRANSFER = 'bank transfer'
    BITCOIN = 'bitcoin'
    OTHER = 'other'

class PaymentOptions(BaseModel):
    payment_method = models.CharField(max_length=255)
    payment_description = models.TextField()
    payment_type = models.CharField(max_length=255, choices=PaymentTypeEnun.choices, default=PaymentTypeEnun.OTHER)
    payment_image = models.ImageField(upload_to='media/payment_options/', null=True, blank=True)

    def __str__(self):
        return f'{self.payment_method}'

class PaymentStatusEnun(models.TextChoices):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    FAILED = 'failed'
    HOLD = 'hold'
    
class Payment(BaseModel):
    payment_method = models.ForeignKey(PaymentOptions, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=255, choices=PaymentStatusEnun.choices, default=PaymentStatusEnun.PENDING)
    # payment data is now if payment method in not cash on delivery else it is the date of the delevery and payment
    payment_date = models.DateField( null=True, blank=True)
    # payment_date = models.DateField(auto_now_add=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_reference = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE )


    def __str__(self):
        return f'{self.payment_method} - {self.payment_amount}'

class Checkout(BaseModel):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Cart)

    def __str__(self):
        return f'{self.user} - {self.payment} - {self.address}'
