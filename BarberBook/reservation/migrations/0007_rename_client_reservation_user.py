# Generated by Django 4.2.3 on 2023-07-19 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_alter_reservation_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='client',
            new_name='user',
        ),
    ]
