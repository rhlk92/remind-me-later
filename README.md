# Remind me later

    A small reminder api which takes email address or mobile number or both and sets a reminder with a message. The api then reminds over their preferred channel of notification with the message.

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
