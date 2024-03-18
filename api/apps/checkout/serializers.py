from rest_framework import serializers
from .models import Checkout, Address, CheckoutItems
from api.apps.cart.models import Cart
from api.apps.orders.models import Order

class CheckoutCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    checkout_items = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = Checkout
        fields = ["id", "checkout_items", "address", "payment", "user"]

    def create(self, validated_data):
        checkout_items_data = validated_data.pop('checkout_items', None)
        checkout = Checkout.objects.create(**validated_data)
        
        if checkout_items_data:
            for cart_id in checkout_items_data:
                cart = Cart.objects.get(id=cart_id)
                checkout_item = CheckoutItems.objects.create(
                    product=cart.product,
                    quantity=cart.quantity
                )
                checkout.checkout_items.add(checkout_item)
                cart.delete()
        # at this point create a order with orderstatus as pending
        order = Order.objects.create(
            user=validated_data['user'],
            order_status='pending'
        )
        order.order_detail = checkout
        order.save()
        return checkout

class CheckoutSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Checkout
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Address
        fields = "__all__"

