# Generated by Django 3.1 on 2020-09-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_auto_20200901_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionals',
            name='status',
            field=models.CharField(blank=True, choices=[('2', 'Active'), ('1', 'InActive')], max_length=5, null=True),
        ),
    ]
