# Generated by Django 3.0.8 on 2020-08-10 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0003_hostel'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='hosteltype',
            old_name='title',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='hostel',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
