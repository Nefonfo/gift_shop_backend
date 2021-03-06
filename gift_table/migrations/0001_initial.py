# Generated by Django 3.2.9 on 2022-04-27 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductGiftTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift_table', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_gift_table', to='gift_table.gifttable')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_table_product', to='product.product')),
            ],
            options={
                'unique_together': {('gift_table', 'product')},
            },
        ),
    ]
