# Generated by Django 2.1.1 on 2018-10-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duradiff', '0023_remove_salary_miscellaneous'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='miscellaneous',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
