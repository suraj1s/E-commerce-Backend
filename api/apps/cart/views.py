from django.shortcuts import render
from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer, CartGetSerializer

class CartListAPIView(generics.ListAPIView):
    serializer_class = CartGetSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
class CartCreateAPIView(generics.CreateAPIView):
    
    serializer_class = CartSerializer
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # print(self.request.user.id)
        # print(self.request.user)
        serializer.save(user=self.request.user)

class CartRetrieveAPIView(generics.RetrieveAPIView):
    
    serializer_class = CartGetSerializer
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartUpdateAPIView(generics.UpdateAPIView):
    
    serializer_class = CartSerializer
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartDeleteAPIView(generics.DestroyAPIView):
    
    serializer_class = CartSerializer
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)