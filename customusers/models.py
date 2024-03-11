from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    AbstractUser._meta.get_field("email")._unique = True
    AbstractUser._meta.get_field("username")._unique = True
    pass