from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from lms.models import Subscription


@shared_task
def send_course_update_notification(course_id):
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
