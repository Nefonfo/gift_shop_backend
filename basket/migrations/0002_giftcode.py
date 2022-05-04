# Generated by Django 3.2.9 on 2022-04-27 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Code')),
                ('mount', models.FloatField(verbose_name='Mount')),
                ('basket', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='basket.basket')),
            ],
        ),
    ]
