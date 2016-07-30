from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_reminder
from .models import Reminder


@receiver(post_save, sender=Reminder)
def reminder_handler(sender, instance, **kwargs):
    """
    create a email task.
    """
    if instance.medium == 'email':
        send_reminder.apply_async(eta=instance.datetime,
                                  kwargs={'pk': instance.pk})
