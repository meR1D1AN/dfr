from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    photo = models.ImageField(
        upload_to="lms/course_photos",
        verbose_name="Фото",
        help_text="Загрузите фото курса",
        **NULLABLE,
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Укажите описание курса", **NULLABLE
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец курса",
        help_text="Укажите владельца курса",
        related_name="owned_courses",
        **NULLABLE,
    )

    def __str__(self):
        return f"Курс {self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Укажите курс",
        related_name="lessons",
        **NULLABLE,
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока", help_text="Укажите описание урока", **NULLABLE
    )
    photo = models.ImageField(
        upload_to="lms/lesson_photos",
        verbose_name="Фото",
        help_text="Загрузите фото",
        **NULLABLE,
    )
    link_video = models.URLField(
        verbose_name="Ссылка на видео", help_text="Укажите ссылку на видео", **NULLABLE
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец урока",
        help_text="Укажите владельца урока",
        related_name="owned_lessons",
        **NULLABLE,
    )

    def __str__(self):
        return f"Урок {self.name}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
