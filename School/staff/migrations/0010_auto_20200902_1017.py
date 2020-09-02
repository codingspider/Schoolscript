# Generated by Django 3.1 on 2020-09-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_auto_20200901_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyinformation',
            name='marrige_day',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='familyinformation',
            name='nid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='professionals',
            name='gender',
            field=models.CharField(choices=[('0', 'Select '), ('1', 'Male'), ('2', 'female'), ('3', 'Others')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='professionals',
            name='status',
            field=models.CharField(choices=[('2', 'Active'), ('1', 'InActive')], max_length=5, null=True),
        ),
    ]
