# Generated by Django 3.2.9 on 2022-04-26 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientaddress',
            name='additional_notes',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Additional Notes'),
        ),
        migrations.AlterField(
            model_name='clientaddress',
            name='int_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Internal Number'),
        ),
    ]
