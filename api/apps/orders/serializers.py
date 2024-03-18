from rest_framework import serializers
from .models import Order
from api.apps.checkout.models import Checkout, CheckoutItems


class CheckoutItemsSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = CheckoutItems
        fields = ["id", "product", "quantity"]

    def get_product(self, obj):
        return {
            'id': obj.product.id,
            'title': obj.product.title,
            'price': obj.product.price,
            'discount': obj.product.discountPercentage,
            'thumbnail': obj.product.thumbnail,
        }

class CheckoutGetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    checkout_items = CheckoutItemsSerializer(many=True)
    class Meta:
        model = Checkout
        fields = ["id", "checkout_items", "address", "payment", "user"]


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    order_detail = CheckoutGetSerializer()  # Instantiate the serializer class
    class Meta:
        model = Order
        fields = ["id", "order_status", "order_detail", "user"]


# for these modal

# class Order (BaseModel):
#     order_status = models.CharField(max_length=255, choices=OrderEnum.choices, default=OrderEnum.PENDING)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     order_detail = models.ForeignKey(Checkout, on_delete=models.CASCADE)
#     def __str__(self):
#         return f'{self.user}  - {self.order_status}'

# class CheckoutItems (BaseModel):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f'{self.product} - {self.quantity}'

# class Checkout(BaseModel):
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)
#     payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     checkout_items = models.ManyToManyField(CheckoutItems)
#     def __str__(self):
#         return f'{self.user} - {self.payment} - {self.address}'



