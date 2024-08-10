from django.conf import settings
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
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
        **NULLABLE
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Цена курса"
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
        verbose_name="Описание урока",
        help_text="Укажите описание урока",
        **NULLABLE
    )
    photo = models.ImageField(
        upload_to="lms/lesson_photos",
        verbose_name="Фото",
        help_text="Загрузите фото",
        **NULLABLE,
    )
    link_video = models.URLField(
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
        **NULLABLE
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


class Subscription(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="subscriptions",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="subscriptions",
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        unique_together = ("user", "course")

    def __str__(self):
        return f"{self.user} подписался на курс {self.course}"


class Payment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="payments"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        related_name="payments"
    )
    stripe_product_id = models.CharField(
        max_length=255,
        verbose_name="ID продукта",
        **NULLABLE
    )
    stripe_price_id = models.CharField(
        max_length=255,
        verbose_name="ID цены",
        **NULLABLE
    )
    stripe_session_id = models.CharField(
        max_length=255,
        verbose_name="ID сессии",
        **NULLABLE
    )
    payment_url = models.URLField(
        max_length=400,
        verbose_name="Ссылка на оплату",
        **NULLABLE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Оплата {self.course.name} от {self.user.email}"

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return f"{self.amount}"
