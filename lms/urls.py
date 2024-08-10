from django.urls import include, path
from rest_framework.routers import DefaultRouter

from lms.views import (
    CourseViewSet,
    LessonDestroyAPIView,
    LessonListCreateAPIView,
    LessonRetrieveUpdateAPIView,
    SubscriptionAPIView, CreatePaymentView,
)

router = DefaultRouter()
router.register(r"courses", CourseViewSet)

app_name = "lms"

urlpatterns = [
    path("", include(router.urls)),
    path("lessons/", LessonListCreateAPIView.as_view(), name="lesson_list_create"),
    path("lessons/<int:pk>/", LessonRetrieveUpdateAPIView.as_view(), name="lesson_detail"),
    path("lessons/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"),
    path("subscriptions/", SubscriptionAPIView.as_view(), name="subscription"),
    path("create_payment/", CreatePaymentView.as_view(), name="create_payment"),
]
