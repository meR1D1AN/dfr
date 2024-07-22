from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UserViewSet, UserCreateView, UserRetrieveUpdateDestroyAPIView

router = DefaultRouter()
router.register(r"users", UserViewSet)

app_name = UsersConfig.name

urlpatterns = [
    path("", include(router.urls), name="users"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("users/<int:pk>/", UserRetrieveUpdateDestroyAPIView.as_view(), name="user_detail"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
