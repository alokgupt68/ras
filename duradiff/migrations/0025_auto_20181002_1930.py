# Generated by Django 2.1.1 on 2018-10-02 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duradiff', '0024_salary_miscellaneous'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salary',
            old_name='miscellaneous',
            new_name='splallowance',
        ),
    ]
