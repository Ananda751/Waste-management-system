# Generated by Django 4.2.2 on 2023-08-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='id',
        ),
        migrations.AlterField(
            model_name='admin',
            name='username',
            field=models.CharField(max_length=122, primary_key=True, serialize=False, unique=True),
        ),
    ]
