# Generated by Django 3.1 on 2020-08-18 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0012_auto_20200818_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='iso',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='iso3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='nicename',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='numcode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='phonecode',
            field=models.IntegerField(null=True),
        ),
    ]
