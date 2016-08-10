from rest_framework import mixins
from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer


class ReminderList(mixins.CreateModelMixin,
                   generics.GenericAPIView):
        queryset = Reminder.objects.all()
        serializer_class = ReminderSerializer

        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)
