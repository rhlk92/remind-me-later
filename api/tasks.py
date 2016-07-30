from celery.decorators import task
from django.conf import settings
from django.core.mail import send_mail
from .models import Reminder


@task
def send_reminder(pk):
    """
    send email to user.
    """
    remind = Reminder.objects.get(pk=pk)
    body = remind.message
    to = [remind.email, ]
    sender = settings.EMAIL_HOST_USER
    subject = "Your Reminder"
    send_mail(subject, body, sender, to, fail_silently=False)
