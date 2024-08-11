from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

from lms.services import send_tg_message
from users.models import User


@shared_task
def send_email_like(email):
    """
    Отправляет письмо, когда уроку поставили лайк
    """
    message = "На урок поставили лайк"
    # send_mail(
    #     "Поставили лайк",
    #     message,
    #     EMAIL_HOST_USER,
    #     [email],
    # )
    user = User.objects.get(email=email)
    if user.tg_chat_id:
        print(user.tg_chat_id)
        send_tg_message(user.tg_chat_id, message)


@shared_task
def send_email_birthday_lesson():
    today = timezone.now().today().date()
    print(today)
