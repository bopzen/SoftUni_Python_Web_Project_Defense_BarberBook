from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

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

    about = models.TextField(
        null=True,
        blank=True
    )

    slug = models.SlugField(
        unique=True
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)