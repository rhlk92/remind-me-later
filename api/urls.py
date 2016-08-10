from django.conf.urls import include, patterns, url
from rest_framework.routers import DefaultRouter
from .views import ReminderViewSet

router = DefaultRouter()
router.register(r'reminders', ReminderViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
