from django.shortcuts import render
from rest_framework import generics
from .models import Payment, PaymentOptions
from .serializers import PaymentSerializer, PaymentOptionsSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

class PaymentCreateAPIView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class PaymentOptionsListAPIView(generics.ListAPIView):
    serializer_class = PaymentOptionsSerializer
    queryset = PaymentOptions.objects.all()

