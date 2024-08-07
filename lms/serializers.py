from rest_framework import serializers

from lms.models import Course, Lesson
from lms.validators import YouTubeValidators


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer  ):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [YouTubeValidators(field="link_video")]