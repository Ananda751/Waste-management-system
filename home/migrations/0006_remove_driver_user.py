# Generated by Django 4.2.2 on 2023-08-05 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_driver_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='user',
        ),
    ]
