# Generated by Django 2.0.5 on 2018-05-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duradiff', '0018_auto_20180506_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='data',
            field=models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg', upload_to=''),
        ),
    ]