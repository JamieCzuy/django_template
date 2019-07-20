# Create Custom User Model

From the root of the repo:

1. Change to src folder:
```
cd src
```

2. Create the User class in the users app's models
Use your editor to create the User class in the users app's models:

In `/users/models.py` lines 1 thru 3.

Change this:
```
from django.db import models

# Create your models here.
```

To this:
```
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
```

4. Use your editor to make this user model the auth user model:

In `/todo/settings.py` add this line below the ALLOWED_HOSTS line - after line 29.
```
AUTH_USER_MODEL = "users.User"
```

5. Use your editor to create User Create and User Change forms

Create file `/users/forms.py` with this content:
```
from django.contrib.auth import forms
from users.models import User


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
        fields = ("username", "email")


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
```

6. Use your editor to create a custom UserAdmin app

Rewrite `/users/admin.py`

Change this:
```
from django.contrib import admin

# Register your models here.
```

To this:
```
from django.contrib import admin
from django.contrib import auth

from users.forms import UserChangeForm
from users.forms import UserCreationForm
from users.models import User


@admin.register(User)
class UserAdmin(auth.admin.UserAdmin):
    add_form = UserChangeForm
    form = UserCreationForm
    list_display = ["email", "username"]
```

7. Verify `manage.py` runs
```
pipenv run python manage.py
```

Should see the usual list of Available subcommands

