# Generated by Django 2.1 on 2020-04-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='approved',
        ),
        migrations.AddField(
            model_name='profile',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
