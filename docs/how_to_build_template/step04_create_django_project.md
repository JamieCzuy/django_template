# Create Django Project

From the root of the repo:

1. Create src folder and change to it:
```bash
mkdir src
cd src
```

2. Run django_admin to create Project:
```bash
pipenv run django-admin startproject todo .
```

3. Verify these files were created:
```bash
find .
```
Should see:
```text
.
./todo
./todo/__init__.py
./todo/settings.py
./todo/urls.py
./todo/wsgi.py
./manage.py
```

4. Verify `manage.py` runs:
```bash
pipenv run python manage.py
```
Should see a list of available commands:
```text
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
