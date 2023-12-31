from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):

    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
