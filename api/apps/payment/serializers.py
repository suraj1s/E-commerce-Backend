from rest_framework import serializers
from .models import  Payment, PaymentOptions



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

