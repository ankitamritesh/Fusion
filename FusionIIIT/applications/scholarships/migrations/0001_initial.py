# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-28 12:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0001_initial'),
        ('academic_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('application_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('applied_flag', models.BooleanField(default=False)),
                ('award', models.CharField(max_length=30)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
            options={
                'db_table': 'Application',
            },
        ),
        migrations.CreateModel(
            name='Award_and_scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(default='', max_length=100)),
                ('catalog', models.TextField(max_length=5000)),
            ],
            options={
                'db_table': 'Award_and_scholarship',
            },
        ),
        migrations.CreateModel(
            name='Director_gold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Complete', 'COMPLETE'), ('Incomplete', 'INCOMPLETE'), ('Reject', 'REJECT'), ('Accept', 'ACCEPT')], default='INCOMPLETE', max_length=10)),
                ('relevant_document', models.FileField(blank=True, null=True, upload_to='')),
                ('date', models.DateField(default=datetime.date.today)),
                ('academic_achievements', models.TextField(max_length=1000, null=True)),
                ('science_inside', models.TextField(max_length=1000, null=True)),
                ('science_outside', models.TextField(max_length=1000, null=True)),
                ('games_inside', models.TextField(max_length=1000, null=True)),
                ('games_outside', models.TextField(max_length=1000, null=True)),
                ('cultural_inside', models.TextField(max_length=1000, null=True)),
                ('cultural_outside', models.TextField(max_length=1000, null=True)),
                ('social', models.TextField(max_length=1000, null=True)),
                ('coorporate', models.TextField(max_length=1000, null=True)),
                ('hall_activities', models.TextField(max_length=1000, null=True)),
                ('gymkhana_activities', models.TextField(max_length=1000, null=True)),
                ('institute_activities', models.TextField(max_length=1000, null=True)),
                ('counselling_activities', models.TextField(max_length=1000, null=True)),
                ('other_activities', models.TextField(max_length=1000, null=True)),
                ('justification', models.TextField(max_length=1000, null=True)),
                ('correspondence_address', models.CharField(max_length=100, null=True)),
                ('financial_assistance', models.TextField(max_length=1000, null=True)),
                ('grand_total', models.IntegerField(null=True)),
                ('nearest_policestation', models.CharField(max_length=25, null=True)),
                ('nearest_railwaystation', models.CharField(max_length=25, null=True)),
                ('award_id', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='scholarships.Award_and_scholarship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
            options={
                'db_table': 'Director_gold',
            },
        ),
        migrations.CreateModel(
            name='Director_silver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Complete', 'COMPLETE'), ('Incomplete', 'INCOMPLETE'), ('Reject', 'REJECT'), ('Accept', 'ACCEPT')], default='INCOMPLETE', max_length=10)),
                ('relevant_document', models.FileField(blank=True, null=True, upload_to='')),
                ('date', models.DateField(default=datetime.date.today)),
                ('inside_achievements', models.TextField(max_length=1000, null=True)),
                ('justification', models.TextField(max_length=1000, null=True)),
                ('outside_achievements', models.TextField(max_length=1000, null=True)),
                ('correspondence_address', models.CharField(max_length=100, null=True)),
                ('financial_assistance', models.TextField(max_length=1000, null=True)),
                ('grand_total', models.IntegerField(null=True)),
                ('nearest_policestation', models.CharField(max_length=25, null=True)),
                ('nearest_railwaystation', models.CharField(max_length=25, null=True)),
                ('award_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarships.Award_and_scholarship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
            options={
                'db_table': 'Director_silver',
            },
        ),
        migrations.CreateModel(
            name='Mcm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brother_name', models.CharField(max_length=30, null=True)),
                ('brother_occupation', models.TextField(max_length=100, null=True)),
                ('sister_name', models.CharField(max_length=30, null=True)),
                ('sister_occupation', models.TextField(max_length=100, null=True)),
                ('income_father', models.IntegerField(default=0)),
                ('income_mother', models.IntegerField(default=0)),
                ('income_other', models.IntegerField(default=0)),
                ('father_occ', models.CharField(choices=[('government', 'Government'), ('private', 'Private'), ('public', 'Public'), ('business', 'Business'), ('medical', 'Medical'), ('consultant', 'Consultant'), ('pensioners', 'Pensioners')], default='', max_length=10)),
                ('mother_occ', models.CharField(choices=[('EMPLOYED', 'EMPLOYED'), ('HOUSE_WIFE', 'HOUSE_WIFE')], default='', max_length=10)),
                ('father_occ_desc', models.CharField(max_length=30, null=True)),
                ('mother_occ_desc', models.CharField(max_length=30, null=True)),
                ('four_wheeler', models.IntegerField(blank=True, null=True)),
                ('four_wheeler_desc', models.CharField(max_length=30, null=True)),
                ('two_wheeler', models.IntegerField(blank=True, null=True)),
                ('two_wheeler_desc', models.CharField(max_length=30, null=True)),
                ('house', models.CharField(max_length=10, null=True)),
                ('plot_area', models.IntegerField(blank=True, null=True)),
                ('constructed_area', models.IntegerField(blank=True, null=True)),
                ('school_fee', models.IntegerField(blank=True, null=True)),
                ('school_name', models.CharField(max_length=30, null=True)),
                ('bank_name', models.CharField(max_length=100, null=True)),
                ('loan_amount', models.IntegerField(blank=True, null=True)),
                ('college_fee', models.IntegerField(blank=True, null=True)),
                ('college_name', models.CharField(max_length=30, null=True)),
                ('income_certificate', models.FileField(blank=True, null=True, upload_to='')),
                ('forms', models.FileField(blank=True, null=True, upload_to='')),
                ('status', models.CharField(choices=[('Complete', 'COMPLETE'), ('Incomplete', 'INCOMPLETE'), ('Reject', 'REJECT'), ('Accept', 'ACCEPT')], default='INCOMPLETE', max_length=10)),
                ('annual_income', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('award_id', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='scholarships.Award_and_scholarship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mcm_info', to='academic_information.Student')),
            ],
            options={
                'db_table': 'Mcm',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_mcm_flag', models.BooleanField(default=False)),
                ('notification_convocation_flag', models.BooleanField(default=False)),
                ('invite_mcm_accept_flag', models.BooleanField(default=False)),
                ('invite_covocation_accept_flag', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Notification',
            },
        ),
        migrations.CreateModel(
            name='Notional_prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spi', models.FloatField()),
                ('cpi', models.FloatField()),
                ('year', models.CharField(choices=[('UG1', 'UG1'), ('UG2', 'UG2'), ('UG3', 'UG3'), ('UG4', 'UG4'), ('PG1', 'PG1'), ('PG2', 'PG2')], max_length=10)),
                ('award_id', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='scholarships.Award_and_scholarship')),
            ],
            options={
                'db_table': 'Notional_prize',
            },
        ),
        migrations.CreateModel(
            name='Previous_winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programme', models.CharField(default='B.Tech', max_length=10)),
                ('year', models.IntegerField(default=2019)),
                ('award_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarships.Award_and_scholarship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
            options={
                'db_table': 'Previous_winner',
            },
        ),
        migrations.CreateModel(
            name='Proficiency_dm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relevant_document', models.FileField(blank=True, null=True, upload_to='')),
                ('title_name', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(choices=[('Complete', 'COMPLETE'), ('Incomplete', 'INCOMPLETE'), ('Reject', 'REJECT'), ('Accept', 'ACCEPT')], default='INCOMPLETE', max_length=10)),
                ('no_of_students', models.IntegerField(default=1)),
                ('date', models.DateField(default=datetime.date.today)),
                ('roll_no1', models.IntegerField(default=0)),
                ('roll_no2', models.IntegerField(default=0)),
                ('roll_no3', models.IntegerField(default=0)),
                ('roll_no4', models.IntegerField(default=0)),
                ('roll_no5', models.IntegerField(default=0)),
                ('brief_description', models.TextField(max_length=1000, null=True)),
                ('justification', models.TextField(max_length=1000, null=True)),
                ('ece_topic', models.CharField(max_length=25, null=True)),
                ('cse_topic', models.CharField(max_length=25, null=True)),
                ('mech_topic', models.CharField(max_length=25, null=True)),
                ('design_topic', models.CharField(max_length=25, null=True)),
                ('ece_percentage', models.IntegerField(null=True)),
                ('cse_percentage', models.IntegerField(null=True)),
                ('mech_percentage', models.IntegerField(null=True)),
                ('design_percentage', models.IntegerField(null=True)),
                ('correspondence_address', models.CharField(max_length=100, null=True)),
                ('financial_assistance', models.TextField(max_length=1000, null=True)),
                ('grand_total', models.IntegerField(null=True)),
                ('nearest_policestation', models.CharField(max_length=25, null=True)),
                ('nearest_railwaystation', models.CharField(max_length=25, null=True)),
                ('award_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarships.Award_and_scholarship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
            options={
                'db_table': 'Proficiency_dm',
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('programme', models.CharField(default='B.Tech', max_length=10)),
                ('startdate', models.DateField(default=datetime.date.today)),
                ('enddate', models.DateField()),
                ('award', models.CharField(default='', max_length=25)),
                ('remarks', models.TextField(default='', max_length=500)),
                ('batch', models.TextField(default='all')),
                ('notif_visible', models.IntegerField(default=1)),
                ('award_form_visible', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Release',
            },
        ),
        migrations.AddField(
            model_name='notification',
            name='release_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='scholarships.Release'),
        ),
        migrations.AddField(
            model_name='notification',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student'),
        ),
    ]