from django.shortcuts import render
from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer, CartGetSerializer
from rest_framework.permissions import IsAuthenticated


class CartListAPIView(generics.ListAPIView):
    serializer_class = CartGetSerializer
    # queryset = Cart.objects.all()

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
class CartCreateAPIView(generics.CreateAPIView):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
        

    def perform_create(self, serializer):
        # print(self.request.user.id)
        # print(self.request.user)
        serializer.save(user=self.request.user)

class CartRetrieveAPIView(generics.RetrieveAPIView):
    # queryset = Cart.objects.all()
    serializer_class = CartGetSerializer
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
        

class CartUpdateAPIView(generics.UpdateAPIView):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
        

class CartDeleteAPIView(generics.DestroyAPIView):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
        
