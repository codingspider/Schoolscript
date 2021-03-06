# Generated by Django 3.0.8 on 2020-08-18 04:18

import announcement.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('announcement', '0003_auto_20200816_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='notice', validators=[announcement.models.validate_file]),
        ),
        migrations.AlterField(
            model_name='notice',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_for',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='status',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], null=True),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('active_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='notice', validators=[announcement.models.validate_file])),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('notice_for', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group')),
            ],
        ),
    ]
