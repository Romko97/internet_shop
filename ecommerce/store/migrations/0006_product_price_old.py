# Generated by Django 3.1.1 on 2020-10-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200929_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_Old',
            field=models.DecimalField(decimal_places=2, default=False, max_digits=7),
        ),
    ]