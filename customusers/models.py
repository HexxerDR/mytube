from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.apps import apps


class CustomUser(AbstractUser):
    AbstractUser._meta.get_field("email")._unique = True
    AbstractUser._meta.get_field("username")._unique = True
    verToken = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    subscriberstotal = models.BigIntegerField(default = 0)
