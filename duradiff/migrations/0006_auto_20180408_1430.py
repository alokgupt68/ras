# Generated by Django 2.0.1 on 2018-04-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duradiff', '0005_auto_20180408_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='OT',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='hrsworked',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
