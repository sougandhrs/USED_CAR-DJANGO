# Generated by Django 4.2.6 on 2024-02-18 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_accessory'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='accessory_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='accessory_images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='accessory_images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='accessory_images/')),
                ('accessory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='users.accessory')),
            ],
        ),
    ]
