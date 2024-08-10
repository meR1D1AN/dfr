from django.contrib.auth.models import AbstractUser
from django.db import models

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


class Donat(models.Model):
    amount = models.PositiveIntegerField(
        verbose_name="Сумма",
        help_text="Укажите сумму",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
        related_name="donats",
    )
    link = models.URLField(
        max_length=400,
        verbose_name="Ссылка на донат",
        help_text="Укажите ссылку на донат",
    )

    class Meta:
        verbose_name = "Донат"
        verbose_name_plural = "Донаты"

    def __str__(self):
        return f"{self.amount}"