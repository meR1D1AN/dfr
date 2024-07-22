from django.urls import include, path
from rest_framework.routers import DefaultRouter

from lms.views import (CourseViewSet, LessonListCreateAPIView,
                       LessonRetrieveUpdateAPIView,
                       LessonDestroyAPIView)

router = DefaultRouter()
router.register(r"courses", CourseViewSet)

app_name = "lms"

urlpatterns = [
    path("", include(router.urls)),
    path("lessons/", LessonListCreateAPIView.as_view(), name="lesson_list_create"),
    path("lessons/<int:pk>/", LessonRetrieveUpdateAPIView.as_view(), name="lesson_detail"),
    path("lessons/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"),
]
