# Create Django Project

From the root of the repo:

1. Create src folder and change to it:
```
mkdir src
cd src
```

2. Run django_admin to create Project:
```
pipenv run django-admin startproject todo .
```

3. Verify these files were created:
```
find .
```
Should see:
```
.
./todo
./todo/__init__.py
./todo/settings.py
./todo/urls.py
./todo/wsgi.py
./manage.py
```

4. Verify `manage.py` runs:
```
pipenv run python manage.py
```
Should see a list of available commands

