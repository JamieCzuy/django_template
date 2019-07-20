# Create Users App

From the root of the repo:

1. Change to src folder:
```
cd src
```

2. Run manage.pyto create Users app:
```
pipenv run python manage.py startapp users
```

3. Verify these files were created:
```
find users
```
Should see:
```
users
users/migrations
users/migrations/__init__.py
users/models.py
users/__init__.py
users/apps.py
users/admin.py
users/tests.py
users/views.py
```

4. Use your editor to add the UsersConfig app to project:

In `/todo/settings.py` lines 33 thru 40.

Change this:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```
To this:
```
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
     'users.apps.UsersConfig',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
```

5. Verify `manage.py` runs:
```
pipenv run python manage.py
```
Should see the following list of available commands
```

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```

