from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class ClientProfile(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    last_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    city = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    phone = models.CharField(
        max_length=12,
        null=False,
        blank=False
    )

    profile_picture = models.ImageField(
        upload_to='profile-pictures',
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )