# Generated by Django 3.1.1 on 2020-10-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200929_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=200, null=True),
        ),
    ]