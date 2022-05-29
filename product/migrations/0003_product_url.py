# Generated by Django 3.2.9 on 2022-05-23 02:27

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20220502_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='name', unique=True),
            preserve_default=False,
        ),
    ]