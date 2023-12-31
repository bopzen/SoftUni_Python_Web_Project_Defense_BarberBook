# Generated by Django 4.2.3 on 2023-07-13 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0004_barbershopprofile_barbershop_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BarbershopService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('barbershop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.barbershopprofile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.servicecategory')),
            ],
        ),
    ]
