from django.shortcuts import render
from rest_framework import generics
from .models import Payment, PaymentOptions
from .serializers import PaymentSerializer, PaymentOptionsSerializer
from rest_framework.permissions import IsAuthenticated

class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    # queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

class PaymentCreateAPIView(generics.CreateAPIView):
    # queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PaymentOptionsListAPIView(generics.ListAPIView):
    serializer_class = PaymentOptionsSerializer
    queryset = PaymentOptions.objects.all()
