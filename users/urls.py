from django.urls import include, path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserCreateAPIView, DonatCreateAPIView

# from users.views import UserViewSet, PaymentViewSet

# router = DefaultRouter()
# router.register(r"users", UserViewSet)
# router.register(r"payments", PaymentViewSet)

app_name = UsersConfig.name

urlpatterns = [
    # path("", include(router.urls), name="users"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
    path("donat/", DonatCreateAPIView.as_view(), name="donat"),
]
