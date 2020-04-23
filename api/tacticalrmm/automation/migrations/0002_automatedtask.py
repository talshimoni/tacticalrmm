# Generated by Django 3.0.5 on 2020-04-10 05:41

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
        ('checks', '0005_auto_20200406_1619'),
        ('automation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutomatedTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('run_time_days', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), blank=True, default=list, null=True, size=None)),
                ('run_time_minute', models.IntegerField(blank=True, choices=[(0, '00:00'), (1, '00:15'), (2, '00:30'), (3, '00:45'), (4, '01:00'), (5, '01:15'), (6, '01:30'), (7, '01:45'), (8, '02:00'), (9, '02:15'), (10, '02:30'), (11, '02:45'), (12, '03:00'), (13, '03:15'), (14, '03:30'), (15, '03:45'), (16, '04:00'), (17, '04:15'), (18, '04:30'), (19, '04:45'), (20, '05:00'), (21, '05:15'), (22, '05:30'), (23, '05:45'), (24, '06:00'), (25, '06:15'), (26, '06:30'), (27, '06:45'), (28, '07:00'), (29, '07:15'), (30, '07:30'), (31, '07:45'), (32, '08:00'), (33, '08:15'), (34, '08:30'), (35, '08:45'), (36, '09:00'), (37, '09:15'), (38, '09:30'), (39, '09:45'), (40, '10:00'), (41, '10:15'), (42, '10:30'), (43, '10:45'), (44, '11:00'), (45, '11:15'), (46, '11:30'), (47, '11:45'), (48, '12:00'), (49, '12:15'), (50, '12:30'), (51, '12:45'), (52, '13:00'), (53, '13:15'), (54, '13:30'), (55, '13:45'), (56, '14:00'), (57, '14:15'), (58, '14:30'), (59, '14:45'), (60, '15:00'), (61, '15:15'), (62, '15:30'), (63, '15:45'), (64, '16:00'), (65, '16:15'), (66, '16:30'), (67, '16:45'), (68, '17:00'), (69, '17:15'), (70, '17:30'), (71, '17:45'), (72, '18:00'), (73, '18:15'), (74, '18:30'), (75, '18:45'), (76, '19:00'), (77, '19:15'), (78, '19:30'), (79, '19:45'), (80, '20:00'), (81, '20:15'), (82, '20:30'), (83, '20:45'), (84, '21:00'), (85, '21:15'), (86, '21:30'), (87, '21:45'), (88, '22:00'), (89, '22:15'), (90, '22:30'), (91, '22:45'), (92, '23:00'), (93, '23:15'), (94, '23:30'), (95, '23:45')], null=True)),
                ('run_manually', models.BooleanField(default=False)),
                ('run_on_check_failure', models.BooleanField(default=False)),
                ('retcode', models.IntegerField(blank=True, null=True)),
                ('stdout', models.TextField(blank=True, null=True)),
                ('stderr', models.TextField(blank=True, null=True)),
                ('last_run', models.DateTimeField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autotasks', to='agents.Agent')),
                ('script', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='autoscript', to='checks.Script')),
            ],
        ),
    ]