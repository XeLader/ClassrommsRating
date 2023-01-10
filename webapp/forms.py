from django import forms
from django.contrib.auth.forms import UserCreationForm

from . import models


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = models.Users
        fields = ("username", "email")

class Comm(forms.ModelForm):

    class Meta:
        model = models.Comments
        fields = ("coment", "kabinet")