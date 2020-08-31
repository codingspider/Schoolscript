# Generated by Django 3.1 on 2020-08-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20200831_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionals',
            name='birth_date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='professionals',
            name='joining_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='professionals',
            name='retirement_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
