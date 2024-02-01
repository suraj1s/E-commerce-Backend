from django.urls import path
from .views import (
    ProductListAPIView,
    ProductCreateAPIView,
    ProductRetrieveAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
)

urlpatterns = [
    path("",ProductListAPIView.as_view(), name="product-list-api-endpoint"),
    path("create/",ProductCreateAPIView.as_view(), name="product-create-api-endpoint"),
    path(
        "<uuid:pk>/",
       ProductRetrieveAPIView.as_view(),
        name="product-retrieve-api-endpoint",
    ),
    path(
        "<uuid:pk>/update/",
       ProductUpdateAPIView.as_view(),
        name="product-update-api-endpoint",
    ),
    path(
        "<uuid:pk>/delete/",
       ProductDeleteAPIView.as_view(),
        name="product-delete-api-endpoint",
    ),
]
