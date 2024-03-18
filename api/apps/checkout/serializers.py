
from rest_framework import serializers
from .models import Checkout, Address, Payment, PaymentOptions
from api.apps.cart.models import Cart


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
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Cart.objects.all())
    class Meta:
        model = Checkout
        fields = [ "id", "items", "address", "payment", "user"]

    def create(self, validated_data):
        items = validated_data.pop('items')
        checkout = Checkout.objects.create(**validated_data)
        print(checkout, "checkout items")
        print(items, "items")
        for item in items:
            print(item, "item")     

        return checkout

# class CheckoutCreateAPIView(generics.CreateAPIView):
#     queryset = Checkout.objects.all()
#     serializer_class = CheckoutCreateSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
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

    # check if the payment method is cash on delivery
    # if it is then set the payment status to Incomplete
    def create(self, validated_data):
        payment = Payment.objects.create(**validated_data)
        if payment.payment_method == 'cash on delivery':
            payment.payment_status = 'incomplete'
            payment.payment_date = None
            payment.save()
        return payment

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
