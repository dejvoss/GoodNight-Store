# Generated by Django 3.1.2 on 2021-01-29 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_product_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductReview',
        ),
    ]