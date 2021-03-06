# Generated by Django 3.1 on 2020-09-08 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0020_auto_20200908_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='personal_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=30)),
                ('experience', models.IntegerField(default=0)),
                ('reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostels.registration')),
            ],
        ),
    ]
