# Generated by Django 3.1 on 2020-08-31 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionals',
            name='is_permanent',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
