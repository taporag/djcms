# Generated by Django 2.2.5 on 2019-09-06 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20190906_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Collection'),
        ),
    ]
