# Bastion - Facebook Event Aggregator

This project allows a user to add Facebook user pages (like [Avenue for the Arts](https://www.facebook.com/avenuefortheartsgr/)) and provide a list of their upcoming events.

Users can input `Facebook` page urls from the django admin page.  Every hour, the host can run `python manage.py sync_events` to request events from Facebook and then store them in the database.  Old or outdated entries can be cleaned with `python manage.py purge_expired`. Just add [Heroku](https://devcenter.heroku.com/articles/deploying-python).

## Features

- Flattens Facebook events data in JSON format
- Minimal interface to add new Facebook pages
- Urls that are not recognized as public facebook pages are automatically removed. (on sync)

## Requirements

- Python 3.6+
- A Facebook Developer Access Token

## Develop!
    $ git clone https://github.com/avenueforthearts/bastion.git
    $ cd bastion
    $ python3 -m venv .
    $ bin/pip3 install -r requirements.txt

`bin/python manage.py` to view available django management tasks.  First things first, setup your database!
    $ bin/python manage.py migrate`
    $ bin/python manage.py createsuperuser`
    $ export FACEBOOK_TOKEN=[your real access token]`
    $ export SECRET_TOKEN=$(python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))')`
    $ export DEBUG=True`

Run the server once the database is properly setup
    $ bin/python manage.py runserver`

You can now login to the django backend (locally: localhost:8000/admin) and login with your super user account.  Then you can add Facebook organization objects in the UI.  An example would be:
```
Name: Avenue for the Arts
URL: https://www.facebook.com/avenuefortheartsgr/
```

You can force Event Synchronization, which will populate the Events table, by using:
    $ bin/python manage.py sync_events`

To purge expired events, you can run:
    $ bin/python manage.py purge_expired

## Deployment to Heroku
    $ heroku create
    $ git push heroku master
    $ heroku run python manage.py migrate

## License: MIT

## Further Reading
- [Template Heroku Project](https://github.com/heroku/heroku-django-template) (Thank you!)
- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
