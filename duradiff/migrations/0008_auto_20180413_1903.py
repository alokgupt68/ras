# Generated by Django 2.0.1 on 2018-04-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duradiff', '0007_auto_20180409_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='netsalary',
        ),
        migrations.AlterField(
            model_name='salary',
            name='esiamt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='totalOTamt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
