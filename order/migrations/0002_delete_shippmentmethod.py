# Generated by Django 3.2.9 on 2022-05-28 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShippmentMethod',
        ),
    ]
