
from django.shortcuts import render
from rest_framework import generics
from .models import Checkout, Address
from .serializers import CheckoutSerializer, AddressSerializer, CheckoutCreateSerializer
from rest_framework.permissions import IsAuthenticated


class CheckoutCreateAPIView(generics.CreateAPIView):
<<<<<<< HEAD
    # queryset = Checkout.objects.all()
    serializer_class = CheckoutCreateSerializer

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Checkout.objects.filter(user=self.request.user)

=======
    serializer_class = CheckoutCreateSerializer
    def queryset(self):
        return Checkout.objects.filter(user=self.request.user)
>>>>>>> b82ca752b26f6b75ace6406d59d204e9463ce776
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CheckoutListAPIView(generics.ListAPIView):
    serializer_class = CheckoutSerializer
<<<<<<< HEAD
    # queryset = Checkout.objects.all()

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Checkout.objects.filter(user=self.request.user)

class CheckoutRetrieveAPIView(generics.RetrieveAPIView):
    # queryset = Checkout.objects.all()
=======
    def queryset(self):
        return Checkout.objects.filter(user=self.request.user)

class CheckoutRetrieveAPIView(generics.RetrieveAPIView):
>>>>>>> b82ca752b26f6b75ace6406d59d204e9463ce776
    serializer_class = CheckoutSerializer
    def queryset(self):
        return Checkout.objects.filter(user=self.request.user)

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Checkout.objects.filter(user=self.request.user)

class CheckoutUpdateAPIView(generics.UpdateAPIView):
    # queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    def queryset(self):
        return Checkout.objects.filter(user=self.request.user)

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Checkout.objects.filter(user=self.request.user)

class CheckoutDeleteAPIView(generics.DestroyAPIView):
    # queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    def queryset(self):
        return Checkout.objects.filter(user=self.request.user)

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Checkout.objects.filter(user=self.request.user)

class AddressListAPIView(generics.ListAPIView):
    serializer_class = AddressSerializer
    # queryset = Address.objects.all()

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

class AddressCreateAPIView(generics.CreateAPIView):
    # queryset = Address.objects.all()
    serializer_class = AddressSerializer

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AddressRetrieveAPIView(generics.RetrieveAPIView):
    # queryset = Address.objects.all()
    serializer_class = AddressSerializer
    def queryset(self):
        return Address.objects.filter(user=self.request.user)

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

class AddressUpdateAPIView(generics.UpdateAPIView):
    # queryset = Address.objects.all()
    serializer_class = AddressSerializer
    def queryset(self):
        return Address.objects.filter(user=self.request.user)

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

class AddressDeleteAPIView(generics.DestroyAPIView):
    # queryset = Address.objects.all()
    serializer_class = AddressSerializer

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
