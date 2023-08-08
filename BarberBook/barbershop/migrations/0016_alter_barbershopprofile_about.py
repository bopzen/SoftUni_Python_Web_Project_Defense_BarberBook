# Generated by Django 4.2.3 on 2023-08-08 10:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0015_alter_barbershoppicture_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barbershopprofile',
            name='about',
            field=models.TextField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
