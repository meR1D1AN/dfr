from django.db import models
from lms.models import Course

NULLABLE = {'null': True, 'blank': True}


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", help_text="Укажите курс",
                               related_name='lessons', **NULLABLE)
    name = models.CharField(max_length=255, verbose_name="Название урока", help_text="Укажите название урока")
    description = models.TextField(verbose_name="Описание урока", help_text="Укажите описание урока", **NULLABLE)
    photo = models.ImageField(upload_to="materials/photos", verbose_name="Фото", help_text="Загрузите фото", **NULLABLE)
    link_video = models.URLField(verbose_name="Ссылка на видео", help_text="Укажите ссылку на видео", **NULLABLE)
