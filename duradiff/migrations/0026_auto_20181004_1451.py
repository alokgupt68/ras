# Generated by Django 2.0.5 on 2018-10-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duradiff', '0025_auto_20181002_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='OD',
            field=models.BooleanField(default=False),
        ),
    ]
