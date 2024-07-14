from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название курса", help_text="Укажите название курса")
    photo = models.ImageField(upload_to="lms/photos", verbose_name="Фото", help_text="Загрузите фото курса", **NULLABLE)
    description = models.TextField(verbose_name="Описание курса", help_text="Укажите описание курса", **NULLABLE)

    def __str__(self):
        return f"Курс {self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
