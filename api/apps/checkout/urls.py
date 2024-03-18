from django.urls import path
from .views import (
    CheckoutCreateAPIView,
    CheckoutDeleteAPIView,
    CheckoutListAPIView,
    CheckoutRetrieveAPIView,
    CheckoutUpdateAPIView,
    AddressCreateAPIView,
    AddressListAPIView,
    AddressRetrieveAPIView,
    AddressUpdateAPIView,
    AddressDeleteAPIView,
    PaymentListAPIView,
    PaymentCreateAPIView,
    PaymentOptionsListAPIView,

)

urlpatterns = [
    path("checkout/",CheckoutListAPIView.as_view(), name="checkout-list-api-endpoint"),
    path("checkout/create/",CheckoutCreateAPIView.as_view(), name="checkout-create-api-endpoint"),
    path(
        "checkout/<uuid:pk>/",
        CheckoutRetrieveAPIView.as_view(),
        name="checkout-retrieve-api-endpoint",
    ),
    path(
        "checkout/<uuid:pk>/update/",
        CheckoutUpdateAPIView.as_view(),
        name="checkout-update-api-endpoint",
    ),
    path(
        "checkout/<uuid:pk>/delete/",
        CheckoutDeleteAPIView.as_view(),
        name="checkout-delete-api-endpoint",
    ),
    path("address/",AddressListAPIView.as_view(), name="address-list-api-endpoint"),
    path("address/create/",AddressCreateAPIView.as_view(), name="address-create-api-endpoint"),
    path(
        "address/<uuid:pk>/",
        AddressRetrieveAPIView.as_view(),
        name="address-retrieve-api-endpoint",
    ),
    path(
        "address/<uuid:pk>/update/",
        AddressUpdateAPIView.as_view(),
        name="address-update-api-endpoint",
    ),
    path(
        "address/<uuid:pk>/delete/",
        AddressDeleteAPIView.as_view(),
        name="address-delete-api-endpoint",
    ),
    path("payment/",PaymentListAPIView.as_view(), name="payment-list-api-endpoint"),
    path("payment/create/",PaymentCreateAPIView.as_view(), name="payment-create-api-endpoint"),
    path("payment_options/",PaymentOptionsListAPIView.as_view(), name="payment-options-list-api-endpoint"),
    
]