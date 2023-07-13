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
        if self.name:
            self.slug = slugify(self.name)
        else:
            self.slug = slugify(self.user)
        return super().save(*args, **kwargs)


class ServiceCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Service Categories'
        
    category_name = models.CharField(
        max_length=30
    )

    def __str__(self):
        return self.category_name


class BarbershopService(models.Model):
    service_name = models.CharField(
        max_length=50,
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE
    )

    barbershop = models.ForeignKey(
        BarbershopProfile,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.service_name
