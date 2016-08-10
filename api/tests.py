from django.core.urlresolvers import reverse
from django.test import TestCase, override_settings
from rest_framework import status
from rest_framework.test import APITestCase
from .tasks import send_reminder


class ReminderTests(APITestCase):
    def test_create_reminder(self):
        """
        create a new reminder.
        """
        url = reverse('reminder-list')
        data = {"medium": "email", "phone": "0123456789",
                "datetime": "2016-07-27 00:00:00",
                "message": "this is new messsage", "email": "rhlk92@gmail.com"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {"email": "rhlk92@gmail.com",
                                         "phone": "0123456789",
                                         "message": "this is new messsage",
                                         "datetime":
                                         "2016-07-27T00:00:00+05:30",
                                         "medium": "email"
                                         })
