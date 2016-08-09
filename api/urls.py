from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns(
    'api.views',
    url(r'^reminders/$', 'reminder_list_api', name='reminder_list_api'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
