from django.shortcuts import render
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderCreateAPIView(generics.CreateAPIView):
    
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderRetrieveAPIView(generics.RetrieveAPIView):
    
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderUpdateAPIView(generics.UpdateAPIView):
    
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderDeleteAPIView(generics.DestroyAPIView):
    
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)