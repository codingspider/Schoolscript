# Generated by Django 3.1 on 2020-09-05 04:40

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0003_cruduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
            ],
        ),
        migrations.DeleteModel(
            name='CrudUser',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
