# Generated by Django 3.1 on 2020-08-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0011_auto_20200818_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institute',
            name='city',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='country',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='state',
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
