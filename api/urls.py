from django.contrib import admin
from django.urls import path, include

api_prefix: str = 'api'

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f'{api_prefix}/', include([
        path('v1/', include([
            path("auth/", include('api.apps.auth.urls')),
            path("product/", include('api.apps.product.urls')),
           
        ]))
    ]))
]
