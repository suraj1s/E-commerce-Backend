from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import Payment, PaymentOptions
from .serializers import PaymentSerializer, PaymentOptionsSerializer, InitiatePaymentSerializer, VerifyPaymentSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter

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


class PaymentOptionsListAPIView(generics.ListAPIView):
    serializer_class = PaymentOptionsSerializer
    queryset = PaymentOptions.objects.all()

class InitiatePaymentView(generics.GenericAPIView):
    serializer_class = InitiatePaymentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        response = serializer.validated_data.get('response')

        return Response(response,status=status.HTTP_200_OK)
    
class VerifyPaymentView(generics.GenericAPIView):
    serializer_class = VerifyPaymentSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="pidx",
                location=OpenApiParameter.QUERY,
                description="search query for detail and other entities",
                required=True,
                type=str,
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        pidx = self.request.query_params.get("pidx", "")  # type:ignore
        serializer = self.get_serializer(data={'pidx': pidx})
        serializer.is_valid(raise_exception=True)
        
        response = serializer.validated_data.get('response')

        return Response(response,status=status.HTTP_200_OK)