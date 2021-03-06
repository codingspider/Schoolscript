# Generated by Django 3.0.8 on 2020-08-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='address',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('license', models.CharField(max_length=200)),
                ('year_made', models.DateField(null=True)),
                ('description', models.TextField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ManyToManyField(blank=True, to='transports.Driver')),
            ],
        ),
    ]
