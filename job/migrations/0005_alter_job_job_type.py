# Generated by Django 4.0.2 on 2022-05-05 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Job_Type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=20),
        ),
    ]
