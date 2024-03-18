from django.db import models
from api.apps.common.models import BaseModel
from api.apps.auth.models import CustomUser as User
# from api.apps.checkout.models import Address

# Create your models here.

class PaymentTypeEnun(models.TextChoices):
    CREDIT_CARD = 'credit card'
    DEBIT_CARD = 'debit card'
    PAYPAL = 'paypal'
    CASH_ON_DELIVERY = 'cash on delivery'
    BANK_TRANSFER = 'bank transfer'
    BITCOIN = 'bitcoin'
    OTHER = 'other'

class PaymentStatusEnun(models.TextChoices):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    FAILED = 'failed'
    HOLD = 'hold'
    
class OrderEnum(models.TextChoices):
    CHECKEDOUT = 'checkedout'
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    FAILED = 'failed'
    HOLD = 'hold'



class PaymentOptions(BaseModel):
    payment_method = models.CharField(max_length=255)
    payment_description = models.TextField()
    payment_type = models.CharField(max_length=255, choices=PaymentTypeEnun.choices, default=PaymentTypeEnun.OTHER)
    payment_image = models.ImageField(upload_to='media/payment_options/', null=True, blank=True)

    def __str__(self):
        return f'{self.payment_method}'


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


class Order (BaseModel):
    order_status = models.CharField(max_length=255, choices=OrderEnum.choices, default=OrderEnum.PENDING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # order_detail = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user} - {self.payment} - {self.order_status}'