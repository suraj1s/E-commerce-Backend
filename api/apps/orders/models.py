from django.db import models
from api.apps.common.models import BaseModel
from api.apps.auth.models import CustomUser as User
from api.apps.checkout.models import Checkout

# Create your models here.

class OrderEnum(models.TextChoices):
    CHECKEDOUT = 'checkedout'
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    FAILED = 'failed'
    HOLD = 'hold'


class Order (BaseModel):
    order_status = models.CharField(max_length=255, choices=OrderEnum.choices, default=OrderEnum.PENDING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_detail = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}  - {self.order_status}'