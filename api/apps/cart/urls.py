from django.urls import path
from .views import (
    CartCreateAPIView,
    CartDeleteAPIView,
    CartListAPIView,
    CartRetrieveAPIView,
    CartUpdateAPIView,
)

urlpatterns = [
    path("",CartListAPIView.as_view(), name="cart-list-api-endpoint"),
    path("create/",CartCreateAPIView.as_view(), name="cart-create-api-endpoint"),
    path(
        "<uuid:pk>/",
        CartRetrieveAPIView.as_view(),
        name="cart-retrieve-api-endpoint",
    ),
    path(
        "<uuid:pk>/update/",
        CartUpdateAPIView.as_view(),
        name="cart-update-api-endpoint",
    ),
    path(
        "<uuid:pk>/delete/",
        CartDeleteAPIView.as_view(),
        name="cart-delete-api-endpoint",
    ),
   
]
