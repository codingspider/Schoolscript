# Generated by Django 3.0.8 on 2020-08-16 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('leave', '0004_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='applied_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leave',
            name='apply_status',
            field=models.IntegerField(choices=[(1, 'Advance'), (2, 'Due')], null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group'),
        ),
    ]
