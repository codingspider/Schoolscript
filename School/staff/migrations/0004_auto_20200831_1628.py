# Generated by Django 3.1 on 2020-08-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20200831_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionals',
            name='mpo_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]