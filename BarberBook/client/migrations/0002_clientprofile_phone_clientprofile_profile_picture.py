# Generated by Django 4.2.3 on 2023-07-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='phone',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/client-default-profile-picture.jpg', null=True, upload_to='client-profile-pictures'),
        ),
    ]