# Generated by Django 2.2.5 on 2019-09-05 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customeraddress',
            options={'verbose_name': 'Customer Address', 'verbose_name_plural': 'Customer Addresses'},
        ),
    ]
