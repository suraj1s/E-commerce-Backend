from django.shortcuts import render
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDeleteAPIView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer