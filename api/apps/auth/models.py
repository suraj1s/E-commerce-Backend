from django.contrib.auth.models import AbstractUser
from django.db import models
from api.apps.common.models import BaseModel


class CustomUser(AbstractUser , BaseModel):
    phone_number = models.BigIntegerField(
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.username 