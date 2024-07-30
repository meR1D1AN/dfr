from rest_framework import serializers

from lms.models import Course, Lesson
from lms.validators import validate_danger_words


class LessonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_danger_words])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    name = serializers.CharField(validators=[validate_danger_words])
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ("id", "name", "description", "lessons_count", "lessons")

    def get_lessons_count(self, obj):
        return obj.lessons.count()
