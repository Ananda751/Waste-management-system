# Generated by Django 4.2.2 on 2023-08-09 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_delivery_schedule_delivery_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=500)),
                ('locality', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=20, unique=True)),
                ('longitude', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='complaints/')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.member')),
            ],
        ),
    ]