# Generated by Django 2.1 on 2020-04-04 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_profile_is_registered'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.BigIntegerField()),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.Profile')),
            ],
        ),
    ]
