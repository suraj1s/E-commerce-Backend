
from django.shortcuts import render
from rest_framework import generics
from .models import Checkout, Address
from .serializers import CheckoutSerializer, AddressSerializer, CheckoutCreateSerializer

class CheckoutCreateAPIView(generics.CreateAPIView):
    serializer_class = CheckoutCreateSerializer
    def queryset(self):
        return Checkout.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CheckoutListAPIView(generics.ListAPIView):
    serializer_class = CheckoutSerializer
    def queryset(self):
        return Checkout.objects.filter(user=self.request.user)

class CheckoutRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CheckoutSerializer
    def queryset(self):
        return Checkout.objects.filter(user=self.request.user)

class CheckoutUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CheckoutSerializer
    def queryset(self):
        return Checkout.objects.filter(user=self.request.user)

class CheckoutDeleteAPIView(generics.DestroyAPIView):
    serializer_class = CheckoutSerializer
    def queryset(self):
        return Checkout.objects.filter(user=self.request.user)

class AddressListAPIView(generics.ListAPIView):
    serializer_class = AddressSerializer
    
    @property
    def queryset(self):
        return Address.objects.filter(user=self.request.user)

class AddressCreateAPIView(generics.CreateAPIView):
    serializer_class = AddressSerializer
    def queryset(self):
        return Address.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AddressRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = AddressSerializer
    def queryset(self):
        return Address.objects.filter(user=self.request.user)

class AddressUpdateAPIView(generics.UpdateAPIView):
    serializer_class = AddressSerializer
    def queryset(self):
        return Address.objects.filter(user=self.request.user)

class AddressDeleteAPIView(generics.DestroyAPIView):
    serializer_class = AddressSerializer
    def queryset(self):
        return Address.objects.filter(user=self.request.user)