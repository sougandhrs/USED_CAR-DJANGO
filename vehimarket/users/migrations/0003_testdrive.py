# Generated by Django 4.2.6 on 2023-11-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_carlisting'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_slot', models.CharField(max_length=20)),
                ('is_booked', models.BooleanField(default=False)),
            ],
        ),
    ]
