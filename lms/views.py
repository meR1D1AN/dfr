from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModer, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (IsAuthenticated, ~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsAuthenticated, IsModer | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsAuthenticated, IsOwner | ~IsModer,)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.groups.filter(name="moders").exists():
            return Course.objects.all()
        return Course.objects.filter(owner=self.request.user)


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModer, IsAuthenticated, IsOwner,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.groups.filter(name="moders").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner,)

    def get_queryset(self):
        if self.request.user.groups.filter(name="moders").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer,)

    def get_queryset(self):
        if self.request.user.groups.filter(name="moders").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)
