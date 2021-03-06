# Generated by Django 3.1 on 2020-08-31 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hostels', '0017_auto_20200818_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.IntegerField(blank=True, null=True)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('father_monthly_income', models.FloatField(blank=True, max_length=255, null=True)),
                ('father_qualification', models.CharField(blank=True, max_length=255, null=True)),
                ('father_phone', models.IntegerField(blank=True, null=True)),
                ('father_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('father_nid', models.IntegerField(blank=True, null=True)),
                ('father_passport', models.CharField(blank=True, max_length=255, null=True)),
                ('father_license', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_monthly_income', models.FloatField(blank=True, max_length=255, null=True)),
                ('mother_educational_qualification', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_phone', models.IntegerField(blank=True, null=True)),
                ('mother_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('mother_nid', models.IntegerField(blank=True, null=True)),
                ('mother_passport', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_license', models.CharField(blank=True, max_length=255, null=True)),
                ('nid', models.IntegerField(blank=True, max_length=255, null=True)),
                ('spouse_name', models.CharField(blank=True, max_length=255, null=True)),
                ('spouse_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('marrige_day', models.DateField(blank=True, null=True)),
                ('spouse_education', models.CharField(blank=True, max_length=255, null=True)),
                ('kids', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professionals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[(0, 'Select '), (1, 'Male'), (2, 'female'), (3, 'Others')], max_length=1)),
                ('work_type', models.CharField(choices=[(0, 'Select '), (1, 'Full Time'), (2, 'Half Time'), (3, 'Permanent'), (4, 'Temporary'), (5, 'Contact')], max_length=1)),
                ('monthly_salary', models.FloatField(blank=True, null=True)),
                ('special_for', models.CharField(blank=True, max_length=255, null=True)),
                ('educational_qualification', models.CharField(blank=True, max_length=255, null=True)),
                ('special_training', models.CharField(blank=True, max_length=255, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('retirement_date', models.DateField(blank=True, null=True)),
                ('index_number', models.IntegerField(blank=True, null=True)),
                ('mpo_date', models.DateField(blank=True, null=True)),
                ('staff_id_no', models.IntegerField(blank=True, null=True)),
                ('teacher_email', models.EmailField(max_length=255, null=True)),
                ('teacher_password', models.CharField(max_length=255, null=True)),
                ('teacher_phone', models.IntegerField(blank=True, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('blood_group', models.CharField(choices=[(0, 'Select '), (1, 'A+'), (2, 'A-'), (3, 'B+'), (4, 'B-'), (5, 'O+'), (6, 'O-'), (7, 'AB+'), (8, 'AB-')], max_length=1)),
                ('religion', models.CharField(choices=[(0, 'Select '), (1, 'Islam'), (2, 'Hinduism'), (3, 'Buddhism'), (4, 'Christianity'), (5, 'Jainism')], max_length=1)),
                ('passport', models.CharField(blank=True, max_length=100, null=True)),
                ('nid', models.CharField(blank=True, max_length=255, null=True)),
                ('last_organizing', models.CharField(blank=True, max_length=255, null=True)),
                ('cause_of_leave', models.CharField(blank=True, max_length=255, null=True)),
                ('institute_address', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[(2, 'Active'), (1, 'InActive')], max_length=1)),
                ('house_number', models.CharField(blank=True, max_length=100, null=True)),
                ('road_number', models.CharField(blank=True, max_length=100, null=True)),
                ('village', models.CharField(blank=True, max_length=100, null=True)),
                ('post_office', models.CharField(blank=True, max_length=100, null=True)),
                ('union_name', models.CharField(blank=True, max_length=100, null=True)),
                ('thana', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('post_code', models.CharField(blank=True, max_length=100, null=True)),
                ('is_permanent', models.BooleanField(blank=True, default=True, null=True)),
                ('per_house_number', models.CharField(blank=True, max_length=100, null=True)),
                ('per_road_number', models.CharField(blank=True, max_length=100, null=True)),
                ('per_village', models.CharField(blank=True, max_length=100, null=True)),
                ('per_post_office', models.CharField(blank=True, max_length=100, null=True)),
                ('per_union_name', models.CharField(blank=True, max_length=100, null=True)),
                ('per_thana', models.CharField(blank=True, max_length=100, null=True)),
                ('per_district', models.CharField(blank=True, max_length=100, null=True)),
                ('per_post_code', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostels.designation')),
                ('staff_access', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.group')),
            ],
        ),
    ]
