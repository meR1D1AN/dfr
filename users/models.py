from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
        help_text="Укажите электронную почту",
    )
    phone = models.CharField(
        max_length=35,
        unique=True,
        verbose_name="Номер телефона",
        help_text="Укажите номер телефона",
        **NULLABLE,
    )
    city = models.CharField(
        max_length=100,
        verbose_name="Город",
        help_text="Укажите город",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите Ваш аватар",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="Пользователь",
    )
    payment_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата оплаты",
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        **NULLABLE,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        **NULLABLE,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма оплаты",
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
    )

    def __str__(self):
        return (f"Платёж от {self.user.email} на сумму {self.amount} руб. "
                f"{self.payment_method} был совершен {self.payment_date}")

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платёжи"


class Donat(models.Model):
    amount = models.PositiveIntegerField(
        verbose_name="Сумма пожертвования",
        help_text="Укажите сумму пожертвования",
    )
    session_id = models.CharField(
        max_length=255,
        verbose_name="ID сессии",
        help_text="Укажите ID сессии",
        **NULLABLE
    )
    link = models.URLField(
        max_length=400,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату",
        **NULLABLE
    )
    user_link = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="donats",
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
        **NULLABLE
    )

    def __str__(self):
        return f"Пожертвование на сумму {self.amount} руб."

    class Meta:
        verbose_name = "Пожертвование"
        verbose_name_plural = "Пожертвования"
