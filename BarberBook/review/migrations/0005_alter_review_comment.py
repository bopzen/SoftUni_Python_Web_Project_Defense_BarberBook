# Generated by Django 4.2.3 on 2023-08-06 19:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_alter_review_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
