# Generated by Django 2.1 on 2020-04-10 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_auto_20200410_0725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='city',
            new_name='district',
        ),
    ]