from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@testov.ru")
        self.course = Course.objects.create(
            name="test",
            description="test",
        )
        self.lesson = Lesson.objects.create(
            name="test",
            course=self.course,
            description="test",
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse("lms:lesson_list_create")
        data = {
            "name": "test",
            "course": self.course.pk,
            "description": "test",
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse("lms:lesson_detail", args=(self.lesson.pk,))
        data = {
            "name": "testov",
            "course": self.course.pk,
            "description": "test",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "testov"
        )

    def test_lesson_delete(self):
        url = reverse("lms:lesson_detail", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("lms:lesson_list_create")
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )


class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@testov.ru")
        self.course = Course.objects.create(
            name="test",
            description="test",
        )
        self.lesson = Lesson.objects.create(
            name="test",
            course=self.course,
            description="test",
        )
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), self.course.name
        )

    def test_course_create(self):
        url = reverse("lms:course-list")
        data = {
            "name": "test",
            "description": "test",
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        data = {
            "name": "testov",
            "description": "test",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "testov"
        )

    def test_course_delete(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):
        url = reverse("lms:course-list")
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
