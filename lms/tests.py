# from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from lms.models import Course, Lesson, Subscription
from users.models import User


class LessonTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email="testuser@example.com",
            password="testpassword"
        )
        self.moderator = User.objects.create(
            email="moderator@example.com",
            password="modpassword"
        )
        self.moderator.groups.create(name="moders")
        self.course = Course.objects.create(name="Test Course", owner=self.user)
        self.lesson_data = {
            "name": "Test Lesson",
            "description": "Lesson description",
            "link_video": "https://www.youtube.com/watch?v=testvideo",
            "course": self.course.id,
        }
        self.lesson = Lesson.objects.create(
            name="Test Lesson",
            description="Lesson description",
            link_video="https://www.youtube.com/watch?v=testvideo",
            course=self.course,
            owner=self.user,
        )

    def test_create_lesson(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse("lms:lesson_list_create"), self.lesson_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_lesson(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("lms:lesson_detail", kwargs={"pk": self.lesson.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.lesson.name)

    def test_update_lesson(self):
        self.client.force_authenticate(user=self.user)
        updated_data = self.lesson_data.copy()
        updated_data["name"] = "Updated Lesson"
        response = self.client.put(
            reverse("lms:lesson_detail", kwargs={"pk": self.lesson.pk}),
            updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.name, "Updated Lesson")

    def test_delete_lesson(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse("lms:lesson_delete", kwargs={"pk": self.lesson.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_moderator_can_edit_any_lesson(self):
        self.client.force_authenticate(user=self.moderator)
        updated_data = self.lesson_data.copy()
        updated_data["name"] = "Moderator Updated Lesson"
        response = self.client.put(
            reverse("lms:lesson_detail", kwargs={"pk": self.lesson.pk}),
            updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.name, "Moderator Updated Lesson")

    def test_moderator_cannot_create_lesson(self):
        self.client.force_authenticate(user=self.moderator)
        response = self.client.post(reverse("lms:lesson_list_create"), self.lesson_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_moderator_cannot_delete_lesson(self):
        self.client.force_authenticate(user=self.moderator)
        response = self.client.delete(reverse("lms:lesson_delete", kwargs={"pk": self.lesson.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class SubscriptionTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email="testuser@example.com", password="testpassword")
        self.course = Course.objects.create(name="Test Course", owner=self.user)

    def test_subscribe_to_course(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse("lms:subscription"), {"course_id": self.course.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe_from_course(self):
        self.client.force_authenticate(user=self.user)
        Subscription.objects.create(user=self.user, course=self.course)
        response = self.client.post(reverse("lms:subscription"), {"course_id": self.course.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())
