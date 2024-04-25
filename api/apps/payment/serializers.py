from rest_framework import serializers,exceptions
from .models import  Payment, PaymentOptions
from api.apps.orders.models import Order
from api.apps.auth.models import CustomUser as User
import os
import json
import requests


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
        
        # print(payment.payment_method, "Khalti")
        print(payment, "payment")
        print(payment.payment_method , "payment method")
        # if payment.payment_method == 'khalti':
        return payment

class PaymentOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentOptions
        fields = "__all__"

class InitiatePaymentSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=255,required=True,allow_blank=False)
    order_id = serializers.CharField(max_length=255,required=True,allow_blank=False)
    payment_method_id = serializers.CharField(max_length=255,required=True)
    return_url = serializers.URLField(required=True)
    amount = serializers.FloatField(required=True)

    def validate(self, attrs):
        order_id = attrs.get('order_id',None)
        payment_method_id = attrs.get('payment_method_id',None)
        user_id = attrs.get('user_id',None)

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            raise exceptions.APIException('Order does not exist')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise exceptions.APIException('User does not exist')
        
        try:
            payment_method = PaymentOptions.objects.get(id=payment_method_id)
        except PaymentOptions.DoesNotExist:
            raise exceptions.APIException('Payment method does not exist')

        purchase_order_id = str(order.id)
        purchase_order_name = user.username
        amount = attrs.get('amount',None)
        return_url = attrs.get('return_url',None)
        print(os.environ.get('KHALTI_BASE_URL'))

        url = f'{os.environ.get("KHALTI_BASE_URL")}epayment/initiate/'
        payload = json.dumps({
            "return_url": return_url,
            "website_url": "http://127.0.0.1:8000",
            "amount": amount,
            "purchase_order_id": purchase_order_id,
            "purchase_order_name": purchase_order_name,
            "customer_info":{
                "name":f'{user.username}',
                "email":"test@khalti.com",
                'phone':"9800000001"
            }
        })

        headers = {
            'Authorization': f"key {os.environ.get('KHALTI_SECRET_KEY')}",
            'Content-Type': 'application/json'
        }
        
        response = requests.request("POST",url,headers=headers, data=payload)

        res = json.loads(response.text)
        print(res)
        Payment.objects.create(
            payment_method=payment_method,
            payment_status='pending',
            payment_date=None,
            payment_amount=amount,
            payment_reference=res.get('id'),
            pidx = res['pidx'],
            user=user
        )
        attrs['response'] = res
        return attrs
    

class VerifyPaymentSerializer(serializers.Serializer):

    pidx = serializers.CharField(max_length=255, required=True, allow_blank=False)

    def validate(self, attrs):
        pidx = attrs.get('pidx',None)

        url = f'{os.environ.get("KHALTI_BASE_URL")}epayment/lookup/'

        payload = json.dumps({
            "pidx": pidx,
        })

        headers = {
            'Authorization': f"key {os.environ.get('KHALTI_SECRET_KEY')}",
            'Content-Type': 'application/json'
        }

        response = requests.request("POST",url,headers=headers,data=payload)

        res = json.loads(response.text)

        attrs['response'] = res
        
        try:
            payment = Payment.objects.get(pidx=pidx)
        except Payment.DoesNotExist:
            raise exceptions.APIException('Payment for this announcement, not found')
        
        if res.get('status') == 'Completed':
            payment.payment_status = 'completed'
            payment.save()
        
        return attrs