# Generated by Django 2.2.5 on 2019-09-06 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20190906_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='featured_image',
            field=models.ImageField(blank=True, upload_to='%Y-%m-%d/collections/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured_image',
            field=models.ImageField(blank=True, upload_to='%Y-%m-%d/products/'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='featured_image',
            field=models.ImageField(blank=True, upload_to='%Y-%m-%d/products/'),
        ),
    ]
