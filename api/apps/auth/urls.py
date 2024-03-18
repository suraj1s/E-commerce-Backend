from django.urls import path
from .views import (
    UserCreateAPIView,
    UserDetailAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
    UserListAPIView,
    UserLoginAPIView,
    UserLogoutAPIView,
    MyTokenObtainPairView,
)
from rest_framework_simplejwt.views import( 
    TokenRefreshView,
    TokenVerifyView
    )

urlpatterns = [
    path('token/', MyTokenObtainPairView, name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('signup/', UserCreateAPIView.as_view(), name='user-signup'),
    path('profile/<int:pk>/', UserDetailAPIView.as_view(), name='user-profile'),
    path('profile/<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('profile/<int:pk>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user-logout'),
]