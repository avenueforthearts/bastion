# Bastion - Facebook Events gathering program

The intention of this project was to design a simple way to allow a user to add Facebook user pages (like [Avenue for the Arts](https://www.facebook.com/avenuefortheartsgr/)) and be able to collect all upcoming events going on for that user.

The general process is the user will input `Facebook` page data from the administrator page.  Every hour, Heroku will run the `python manage.py sync_events` to parse through the Facebook page data, grab all upcoming events from them, and then publish the events via JSON for the world to use.


## Features

- Simplifies/flattens Facebook events data in JSON format
- Simple interface to add new Facebook pages
- User/group administration
- Automatically purges invalid Facebook pages. If a page does not provide the correct ID when requested, it will be purged!

## Requirements

- Python 3.6+
- A Facebook Access Token

## How to Use

To use this project, follow these steps:

1. `python3 -m venv .`
2. `bin/pip3 install -r requirements.txt`

Now you can use `bin/python manage.py` to see all the tasks you have available to run.  First things first, we need to setup your database.

1. `bin/python manage.py migrate`
2. `bin/python manage.py createsuperuser`
3. Set the environment variable `FACEBOOK_TOKEN` to your Facebook Access Token

With the database setup, we can now run the server.
1. `bin/python manage.py runserver`

You can now hit your host (if locally, localhost:8000/admin) and login with your super user account.  Then you can add Facebook organization objects in the UI.  An example would be:
```
Name: Avenue for the Arts
URL: https://www.facebook.com/avenuefortheartsgr/
```

You can trigger the Event Synchronization, which will populate the Events table, by using:
1. `bin/python manage.py sync_events`

To purge expired events, you can run:
1. `bin/python manage.py purge_expired`

## Deployment to Heroku

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
