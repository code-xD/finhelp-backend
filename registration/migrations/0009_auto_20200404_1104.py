# Generated by Django 2.1 on 2020-04-04 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20200404_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='approved',
            new_name='status',
        ),
    ]
