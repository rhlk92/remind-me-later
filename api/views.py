from rest_framework import mixins
from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer


class ReminderList(generics.CreateAPIView):
        queryset = Reminder.objects.all()
        serializer_class = ReminderSerializer
