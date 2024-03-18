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


# for this serilizer create the order and make the orderstatus checkedout
# class CheckoutCreateSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(
#         default=serializers.CurrentUserDefault()
#     )
#     checkout_items = serializers.ListField(write_only=True, required=False)

#     class Meta:
#         model = Checkout
#         fields = ["id", "checkout_items", "address", "payment", "user"]

#     def create(self, validated_data):
#         checkout_items_data = validated_data.pop('checkout_items', None)
#         checkout = Checkout.objects.create(**validated_data)
        
#         if checkout_items_data:
#             for cart_id in checkout_items_data:
#                 cart = Cart.objects.get(id=cart_id)
#                 checkout_item = CheckoutItems.objects.create(
#                     product=cart.product,
#                     quantity=cart.quantity
#                 )
#                 checkout.checkout_items.add(checkout_item)
#                 cart.delete()
#         # at this point create a order with orderstatus as pending
#         order = Order.objects.create(
#             user=validated_data['user'],
#             order_status='pending'
#         )
#         order.order_detail = checkout
#         order.save()
#         return checkout

class Order (BaseModel):
    order_status = models.CharField(max_length=255, choices=OrderEnum.choices, default=OrderEnum.PENDING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_detail = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}  - {self.order_status}'