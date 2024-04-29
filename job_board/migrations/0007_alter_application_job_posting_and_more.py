# Generated by Django 5.0.4 on 2024-04-29 00:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0006_alter_application_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='job_posting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to='job_board.jobposting'),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending Review'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected'), ('DELETED', 'Job Posting Deleted')], default='PENDING', max_length=20),
        ),
    ]
