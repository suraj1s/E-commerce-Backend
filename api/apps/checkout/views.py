from django.shortcuts import render
from rest_framework import generics
from .models import Checkout, Address
from .serializers import CheckoutSerializer, AddressSerializer




class CheckoutCreateAPIView(generics.CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class CheckoutListAPIView(generics.ListAPIView):
    serializer_class = CheckoutSerializer
    queryset = Checkout.objects.all()


class CheckoutRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

class CheckoutUpdateAPIView(generics.UpdateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

class CheckoutDeleteAPIView(generics.DestroyAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

class AddressListAPIView(generics.ListAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class AddressCreateAPIView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AddressRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressUpdateAPIView(generics.UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDeleteAPIView(generics.DestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

