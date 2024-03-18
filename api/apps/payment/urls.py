from django.urls import path
from .views import (
    PaymentListAPIView,
    PaymentCreateAPIView,
    PaymentOptionsListAPIView,
)

urlpatterns = [
    path("",PaymentListAPIView.as_view(), name="payment-list-api-endpoint"),
    path("create/",PaymentCreateAPIView.as_view(), name="payment-create-api-endpoint"),
    path("payment_options/",PaymentOptionsListAPIView.as_view(), name="payment-options-list-api-endpoint"),
    
]