# Generated by Django 3.1 on 2020-08-19 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0023_auto_20200819_1000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='wikiData',
            new_name='wiki',
        ),
    ]
