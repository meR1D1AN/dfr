from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth import get_user_model

from config.settings import EMAIL_HOST_USER
from lms.models import Subscription


@shared_task
def send_course_update_notification(course_id):
    """
    Отправляет уведомление об обновлении курса всем подписчикам данного курса.
    Аргументы: course_id (int): ID курса, который был обновлён.
    Возвращает: None
    """
    subject = "Уведомление об обновлении курса"
    subscriptions = Subscription.objects.filter(course_id=course_id)
    for subscription in subscriptions:
        print(subscriptions.user.email)
        send_mail(
            subject=subject,
            message=f'Курс "{subscription.course.name}" был обновлён',
            from_email=EMAIL_HOST_USER,
            recipient_list=[subscription.user.email],
            fail_silently=False,
        )


@shared_task
def deactive_inactive_users():
    """
    Деактивирует пользователей, которые неактивны более 30 дней.
    Эта функция использует Django ORM для получения пользователей, которые не заходили за последние 30 дней
    и в настоящее время активны. Она затем перебирает этих пользователей, устанавливает их статус `is_active` в False
    и сохраняет изменения.
    Параметры: None
    Возвращает: None
    """
    User = get_user_model()
    one_month_ago = timezone.now() - timedelta(days=30)

    inactive_user = User.objects.filter(last_login__lt=one_month_ago, is_active=True)

    for user in inactive_user:
        user.is_active = False
        user.save()
        print(f"Пользователь {user.email} был деактивирован, из-за неактивности более 30 дней")
