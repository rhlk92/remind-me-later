from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ReminderList

urlpatterns = patterns(
    'api.views',
    url(r'^reminders/$', ReminderList.as_view(), name='reminder_list'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
