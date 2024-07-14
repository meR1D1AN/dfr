from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"payments", PaymentViewSet)

app_name = "users"

urlpatterns = [
    path("", include(router.urls), name="users"),
]
