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
