from rest_framework import viewsets
from rest_framework import mixins
from .models import Reminder
from .serializers import ReminderSerializer


class ReminderViewSet(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    """
    create a new reminder.
    """
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
