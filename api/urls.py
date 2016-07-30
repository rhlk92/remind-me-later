from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^reminders/$', 'reminder_list_api', name='reminder_list_api'),
)
