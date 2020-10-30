from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    telegram_user_id = models.CharField(max_length=50, null=True, blank=True)
