from rest_framework.viewsets import ModelViewSet
from .models import Reminder
from .serializers import ReminderSerializer


class ReminderViewSet(ModelViewSet):
    """
    create a new reminder.
    """
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
