# Generated by Django 4.2.3 on 2023-08-04 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0013_alter_barbershopprofile_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barbershoppicture',
            options={'verbose_name_plural': 'Barbershop Pictures'},
        ),
        migrations.AlterModelOptions(
            name='barbershopprofile',
            options={'verbose_name': 'Barbershop Profile'},
        ),
        migrations.AlterModelOptions(
            name='barbershopservice',
            options={'verbose_name_plural': 'Barbershop Services'},
        ),
    ]
