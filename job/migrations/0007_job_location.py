# Generated by Django 4.0.2 on 2022-05-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]
