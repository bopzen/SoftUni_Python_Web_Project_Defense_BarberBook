# Generated by Django 4.2.3 on 2023-07-12 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_clientprofile_phone_clientprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='client-profile-pictures'),
        ),
    ]