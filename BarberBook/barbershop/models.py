import uuid
from datetime import time

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify

UserModel = get_user_model()


class BarbershopProfile(models.Model):
    class Meta:
        verbose_name = 'Barbershop Profile'

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
    geolocation_latitude = models.DecimalField(
        max_digits=18,
        decimal_places=15,
        null=True,
        blank=True
        )
    geolocation_longitude = models.DecimalField(
        max_digits=18,
        decimal_places=15,
        null=True,
        blank=True
        )
    about = models.TextField(
        max_length=200,
        null=True,
        blank=True
    )
    barbershop_picture = models.ImageField(
        upload_to='barbershop-profile-pictures',
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        unique=True
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            for day in range(1, 8):
                BarbershopWorkingHours.objects.create(
                    barbershop=self,
                    day=day,
                    start_time=None,
                    end_time=None
                )
        if self.name:
            self.slug = slugify(self.name)
        else:
            self.name = slugify(self.user)
            self.slug = slugify(self.user)
        super().save(*args, **kwargs)


class ServiceCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Service Categories'

    category_name = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.category_name


class BarbershopService(models.Model):
    class Meta:
        verbose_name_plural = 'Barbershop Services'

    service_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False
    )
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
    )

    barbershop = models.ForeignKey(
        BarbershopProfile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.service_name


class BarbershopWorkingHours(models.Model):
    WEEKDAYS = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    TIME_SLOT_CHOICES = []
    for hour in range(0, 24):
        for minute in range(0, 60, 30):
            time_slot = time(hour, minute)
            display_text = time_slot.strftime('%H:%M')
            TIME_SLOT_CHOICES.append((time_slot, display_text))

    barbershop = models.ForeignKey(
        BarbershopProfile,
        on_delete=models.CASCADE
    )
    day = models.IntegerField(
        choices=WEEKDAYS,
        null=False,
        blank=False
    )
    start_time = models.TimeField(
        choices=TIME_SLOT_CHOICES,
        null=True,
        blank=True
    )
    end_time = models.TimeField(
        choices=TIME_SLOT_CHOICES,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ('barbershop', 'day')
        verbose_name_plural = 'Barbershop Working Hours'

    def clean(self):
        if self.start_time is not None and self.end_time is not None:
            if self.start_time >= self.end_time:
                raise ValidationError('End time must be later than start time.')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


def barbershop_picture_upload_to(instance, filename):
    barbershop_id = instance.barbershop.pk
    upload_filename = f'{uuid.uuid4().hex}.jpg'
    return f'barbershop-pictures/{barbershop_id}/{upload_filename}'


class BarbershopPicture(models.Model):
    class Meta:
        verbose_name_plural = 'Barbershop Pictures'

    barbershop = models.ForeignKey(
        BarbershopProfile,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to=barbershop_picture_upload_to)

    def __str__(self):
        return f'{self.barbershop.name} - {self.image.name}'