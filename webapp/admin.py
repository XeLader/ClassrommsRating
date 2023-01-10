from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

from .forms import CustomUserCreationForm
admin.site.register(models.Users)
admin.site.register(models.Ratings)
admin.site.register(models.Kabinet)
admin.site.register(models.Comments)
# Register your models here.


class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = models.Users
    list_display = ["email", "username"]
