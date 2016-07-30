# Remind me later

RML is a webapp which does only one thing but does this one thing very well. Anybody can open the webapp, provide either their email address or their mobile number or both and setup a reminder with a message. RML then reminds them over their preferred channel of notification with the message.

## Run it!

First start your Redis server
```sh
redis-server
```

Next, start a Celery worker
```sh
python manage.py celeryd
```

Start your Django developement server
```sh
python manage.py runserver
```

## API Endpoint

```sh
GET api/reminders/
```
```sh
{
  "medium": "email",
  "phone": "8969854512",
  "datetime": "2016-07-22 09:01:00",
  "message":"this is messsage",
  "email": "xyz@gmail.com"
}
```
