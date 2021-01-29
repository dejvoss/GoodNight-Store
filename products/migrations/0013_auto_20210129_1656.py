# Generated by Django 3.1.2 on 2021-01-29 15:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20210129_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rate',
            field=models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
