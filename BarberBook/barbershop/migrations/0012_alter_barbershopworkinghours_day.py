# Generated by Django 4.2.3 on 2023-07-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0011_barbershoppicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barbershopworkinghours',
            name='day',
            field=models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')]),
        ),
    ]