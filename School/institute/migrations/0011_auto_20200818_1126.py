# Generated by Django 3.1 on 2020-08-18 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0010_auto_20200818_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='iso',
        ),
        migrations.RemoveField(
            model_name='country',
            name='iso3',
        ),
        migrations.RemoveField(
            model_name='country',
            name='nicename',
        ),
        migrations.RemoveField(
            model_name='country',
            name='numcode',
        ),
        migrations.RemoveField(
            model_name='country',
            name='phonecode',
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
