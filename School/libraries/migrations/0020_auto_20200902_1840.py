# Generated by Django 3.1 on 2020-09-02 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0019_auto_20200829_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookissue',
            name='issued_by',
        ),
        migrations.RemoveField(
            model_name='bookissue',
            name='member',
        ),
    ]
