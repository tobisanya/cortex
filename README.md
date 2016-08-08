[![Stories in Ready](https://badge.waffle.io/WorldBrain/cortex.png?label=ready&title=Ready)](https://waffle.io/WorldBrain/cortex)
# cortex

`cortex` is the back-end server for the [webmarks](https://github.com/WorldBrain/webmarks) project.

It is a [django](https://www.djangoproject.com/) and [django-rest-framework](http://www.django-rest-framework.org/) powered application.

# Installation
Fork this repo and get a local copy with:

```
$ git clone https://github.com/<username>/cortex && cd $_
```

Please [create and activate virtualenv first] (http://docs.python-guide.org/en/latest/dev/virtualenvs/).


We use [pip-tools](https://github.com/nvie/pip-tools) and [pip](https://pip.pypa.io/en/stable/installing/) to manage our requirements:

```
$ pip install -r requirements/development.txt
```

Get a PostgreSQL database and a user up and running:

```
$ sudo -u postgres createdb worldbrain
$ sudo -u postgres psql
postgres=# CREATE USER cortex with PASSWORD 'cortex';
postgres=# GRANT ALL PRIVILEGES ON DATABASE worldbrain to cortex;
postgres=# ALTER USER cortex CREATEDB;
```

You'll then need to export a number of environment variables.

```
export DJANGO_SETTINGS_MODULE="worldbrain.settings.development"
export DJANGO_SECRET_KEY=0123456789abcdefghijklmnopqrstuvwyxz
export DATABASE_NAME=worldbrain
export DATABASE_USER=cortex
export DATABASE_PASSWORD=cortex
```

After that, you can then run:

```
$ python manange.py migrate
$ python manange.py createsuperuser
$ python manage.py runserver
```

Happy hacking!

# Testing
We are using [py.test][pytest] for our testing. You can run them with:

```
$ py.test worldbrain           # test runner
$ ptw worldbrain -- --testmon  # test watcher
```