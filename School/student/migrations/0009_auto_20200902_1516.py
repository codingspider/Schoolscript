# Generated by Django 3.1 on 2020-09-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0004_auto_20200902_1513'),
        ('student', '0008_auto_20200902_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_class',
        ),
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.ManyToManyField(null=True, to='subject.Class'),
        ),
    ]
