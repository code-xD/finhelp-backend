# Generated by Django 2.1 on 2020-04-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20200404_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='profile',
            name='approved',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]