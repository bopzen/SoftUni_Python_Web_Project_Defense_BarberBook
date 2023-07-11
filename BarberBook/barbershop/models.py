from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class BarbershopProfile(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    address = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    city = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )