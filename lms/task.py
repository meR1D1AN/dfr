from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_email_like(email):
    """
    Отправляет письмо, когда уроку поставили лайк
    """
    send_mail(
        "Поставили лайк",
        "На урок постаивли лайк",
        EMAIL_HOST_USER,
        [email],
    )
