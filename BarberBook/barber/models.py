from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Barber(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    about = models.TextField(
        null=False,
        blank=False
    )
    barber_picture = models.ImageField(
        upload_to='barber-pictures',
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING
    )
