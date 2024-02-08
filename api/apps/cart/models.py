from django.db import models
from api.apps.common.models import BaseModel
class Cart(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
   
    class Meta:
        unique_together = ['user', 'product']
    
    def __str__(self):
        return f'{self.user} - {self.product} - {self.quantity}'