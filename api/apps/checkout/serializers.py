from rest_framework import serializers
from .models import Checkout, Address


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

# class AddressGetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = "__all__"
        
#     def get_user(self, obj):
#         request = self.context.get('request')
#         return request.user