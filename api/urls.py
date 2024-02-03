from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

api_prefix: str = 'api'

urlpatterns = [
    path("admin/", admin.site.urls),
     path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path(f'{api_prefix}/', include([
        path('v1/', include([
            # path("auth/", include('api.apps.auth.urls')),
            path("product/", include('api.apps.product.urls')),
           
        ]))
    ]))
]
