from django.urls import path
from .views import (
    OrderListAPIView,
    OrderCreateAPIView,
    OrderRetrieveAPIView,
    OrderUpdateAPIView,
    OrderDeleteAPIView,
)
urlpatterns = [
   path("",OrderListAPIView.as_view(), name="order-list-api-endpoint"),
    path("create/",OrderCreateAPIView.as_view(), name="order-create-api-endpoint"),
    path(
        "<uuid:pk>/",
        OrderRetrieveAPIView.as_view(),
        name="order-retrieve-api-endpoint",
    ),
    path(
        "<uuid:pk>/update/",
        OrderUpdateAPIView.as_view(),
        name="order-update-api-endpoint",
    ),
    path(
        "<uuid:pk>/delete/",
        OrderDeleteAPIView.as_view(),
        name="order-delete-api-endpoint",
    ),

]