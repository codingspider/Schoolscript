# Generated by Django 3.1 on 2020-08-27 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0047_auto_20200827_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='established_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
