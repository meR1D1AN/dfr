from rest_framework import serializers

from lms.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ("id", "name", "description", "lessons_count")

    def get_lessons_count(self, obj):
        return obj.lessons.count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
