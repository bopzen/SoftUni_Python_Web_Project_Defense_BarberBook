# Generated by Django 4.2.3 on 2023-07-17 11:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('barbershop', '0011_barbershoppicture'),
        ('client', '0003_alter_clientprofile_profile_picture'),
        ('barber', '0004_alter_barber_barbershop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField(choices=[(datetime.time(0, 0), '00:00'), (datetime.time(0, 30), '00:30'), (datetime.time(1, 0), '01:00'), (datetime.time(1, 30), '01:30'), (datetime.time(2, 0), '02:00'), (datetime.time(2, 30), '02:30'), (datetime.time(3, 0), '03:00'), (datetime.time(3, 30), '03:30'), (datetime.time(4, 0), '04:00'), (datetime.time(4, 30), '04:30'), (datetime.time(5, 0), '05:00'), (datetime.time(5, 30), '05:30'), (datetime.time(6, 0), '06:00'), (datetime.time(6, 30), '06:30'), (datetime.time(7, 0), '07:00'), (datetime.time(7, 30), '07:30'), (datetime.time(8, 0), '08:00'), (datetime.time(8, 30), '08:30'), (datetime.time(9, 0), '09:00'), (datetime.time(9, 30), '09:30'), (datetime.time(10, 0), '10:00'), (datetime.time(10, 30), '10:30'), (datetime.time(11, 0), '11:00'), (datetime.time(11, 30), '11:30'), (datetime.time(12, 0), '12:00'), (datetime.time(12, 30), '12:30'), (datetime.time(13, 0), '13:00'), (datetime.time(13, 30), '13:30'), (datetime.time(14, 0), '14:00'), (datetime.time(14, 30), '14:30'), (datetime.time(15, 0), '15:00'), (datetime.time(15, 30), '15:30'), (datetime.time(16, 0), '16:00'), (datetime.time(16, 30), '16:30'), (datetime.time(17, 0), '17:00'), (datetime.time(17, 30), '17:30'), (datetime.time(18, 0), '18:00'), (datetime.time(18, 30), '18:30'), (datetime.time(19, 0), '19:00'), (datetime.time(19, 30), '19:30'), (datetime.time(20, 0), '20:00'), (datetime.time(20, 30), '20:30'), (datetime.time(21, 0), '21:00'), (datetime.time(21, 30), '21:30'), (datetime.time(22, 0), '22:00'), (datetime.time(22, 30), '22:30'), (datetime.time(23, 0), '23:00'), (datetime.time(23, 30), '23:30')])),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barber.barber')),
                ('barbershop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.barbershopprofile')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.clientprofile')),
            ],
        ),
    ]
