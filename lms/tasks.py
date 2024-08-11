from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

from lms.models import Lesson


@shared_task
def send_email_like(email):
    """
    Отправляет письмо, когда уроку поставили лайк
    """
    send_mail(
        "Поставили лайк",
        "На урок поставили лайк",
        EMAIL_HOST_USER,
        [email],
    )


@shared_task
def send_email_birthday_lesson():
    today = timezone.now().today().date()
    print(today)
