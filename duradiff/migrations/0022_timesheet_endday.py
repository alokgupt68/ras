# Generated by Django 2.0.5 on 2018-09-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duradiff', '0021_resource_splallowance'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='endday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
