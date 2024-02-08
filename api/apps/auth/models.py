from django.contrib.auth.models import AbstractUser
from django.db import models
from api.apps.common.models import BaseModel

class Address(BaseModel):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.city}, {self.state}, {self.country}'

class CustomUser(AbstractUser , BaseModel):
    phone_number = models.BigIntegerField(
        blank=True,
        null=True,
    )
    addresses = models.ManyToManyField(Address, blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.username