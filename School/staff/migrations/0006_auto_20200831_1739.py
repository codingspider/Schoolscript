# Generated by Django 3.1 on 2020-08-31 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20200831_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionals',
            name='blood_group',
            field=models.CharField(choices=[('0', 'Select '), ('1', 'A+'), ('2', 'A-'), ('3', 'B+'), ('4', 'B-'), ('5', 'O+'), ('6', 'O-'), ('7', 'AB+'), ('8', 'AB-')], max_length=5),
        ),
        migrations.AlterField(
            model_name='professionals',
            name='gender',
            field=models.CharField(choices=[('0', 'Select '), ('1', 'Male'), ('2', 'female'), ('3', 'Others')], max_length=5),
        ),
        migrations.AlterField(
            model_name='professionals',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='staff/'),
        ),
        migrations.AlterField(
            model_name='professionals',
            name='religion',
            field=models.CharField(choices=[('0', 'Select '), ('1', 'Islam'), ('2', 'Hinduism'), ('3', 'Buddhism'), ('4', 'Christianity'), ('5', 'Jainism')], max_length=5),
        ),
        migrations.AlterField(
            model_name='professionals',
            name='status',
            field=models.CharField(choices=[('2', 'Active'), ('1', 'InActive')], max_length=5),
        ),
        migrations.AlterField(
            model_name='professionals',
            name='work_type',
            field=models.CharField(choices=[('0', 'Select '), ('1', 'Full Time'), ('2', 'Half Time'), ('3', 'Permanent'), ('4', 'Temporary'), ('5', 'Contact')], max_length=5),
        ),
    ]
