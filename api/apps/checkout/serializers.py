
from rest_framework import serializers
from .models import Checkout, Address, Payment, PaymentOptions


# here we change the status of the payment to completed and cart to CHECKEDOUT

# this is the old serializer for single cart id
# class CheckoutCreateSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(
#         default=serializers.CurrentUserDefault()
#     )
#     class Meta:
#         model = Checkout
#         fields = [ "id", "item", "address", "payment", "user"]

#     def create(self, validated_data):
#         checkout = Checkout.objects.create(**validated_data)
#         checkout.cart.status = 'CHECKEDOUT'
#         checkout.cart.save()
#         checkout.payment.status = 'COMPLETED'
#         checkout.payment.save()
#         return checkout


# this is the new serializer for multiple cart ids
class CheckoutCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Checkout
        fields = [ "id", "items", "address", "payment", "user"]

    def create(self, validated_data):
        checkout = Checkout.objects.create(**validated_data)
        for cart in checkout.items.all():
            cart.status = 'CHECKEDOUT'
            cart.save()
        checkout.payment.payment_status = 'completed'
        checkout.payment.save()
        return checkout
        
class CheckoutSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Checkout
        fields = "__all__"

# class CheckoutGetSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField()
#     address = serializers.StringRelatedField()
#     payment = serializers.StringRelatedField()
#     items = serializers.StringRelatedField()
#     class Meta:
#         model = Checkout
#         fields = "__all__"
        
#     def get_user(self, obj):
#         request = self.context.get('request')
#         return request.user

class AddressSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Address
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Payment
        fields = "__all__"

class PaymentOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentOptions
        fields = "__all__"

# class AddressGetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = "__all__"
        
#     def get_user(self, obj):
#         request = self.context.get('request')
#         return request.user
