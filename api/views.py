from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import send_reminder
from .serializers import ReminderSerializer
from .models import Reminder


@api_view(['POST'])
def reminder_list_api(request):
    """
    create a new reminder.
    """
    if request.method == 'POST':
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@receiver(post_save, sender=Reminder)
def reminder_handler(sender, instance, **kwargs):
    """
    create a email task.
    """
    if instance.medium == 'email':
        send_reminder.apply_async(eta=instance.datetime,
                                  kwargs={'pk': instance.pk})
