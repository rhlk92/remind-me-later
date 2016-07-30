from django.db import models


class Reminder(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField()
    datetime = models.DateTimeField()
    medium = models.CharField(max_length=100)
