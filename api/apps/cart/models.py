from django.db import models
from api.apps.common.models import BaseModel
from api.apps.product.models import Product
from api.apps.auth.models import CustomUser as User

class CartStatusEnun(models.TextChoices):
    PENDING = 'pending'
    CHECKEDOUT = 'checkedout'
    CANCELLED = 'cancelled'
    SHIPPES = 'shipped'
    DELIVERED = 'delivered'
    
class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=255, choices=CartStatusEnun.choices, default=CartStatusEnun.PENDING)
    
    class Meta:
        unique_together = ['user', 'product']
    
    def __str__(self):
        return f'{self.user}  - {self.quantity}'