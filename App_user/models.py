from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_blocked = models.BooleanField(default=True)
    daily_request_limit = models.PositiveIntegerField(default=0)  # Set an appropriate default limit

    def __str__(self):
        return self.username
