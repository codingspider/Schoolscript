# Generated by Django 3.1 on 2020-08-15 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='institute_logo',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='institute',
            name='principal_signature',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
