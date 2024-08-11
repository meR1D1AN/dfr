from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

import lms
from lms.models import Course, Lesson
from lms.paginations import CustomPagination
from lms.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination

    @action(detail=True, methods=("post",))
    def likes(self, request, pk):
        lesson = self.get_object_or_404(Lesson, pk=pk)
        if lesson.likes.filter(pk=request.user.pk).exists():
            lesson.likes.remove(request.user)
            lms.task.send_email_like.delay()
        else:
            lesson.likes.add(request.user)
            lms.task.send_email_like.delay(lesson.owner.email)
        serializer = self.get_serializer(lesson)
        return Response(data=serializer.data)


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
