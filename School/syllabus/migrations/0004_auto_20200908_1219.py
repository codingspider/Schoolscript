# Generated by Django 3.1 on 2020-09-08 06:19

from django.db import migrations, models
import syllabus.models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0003_auto_20200908_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='ebook', validators=[syllabus.models.validate_file]),
        ),
    ]
