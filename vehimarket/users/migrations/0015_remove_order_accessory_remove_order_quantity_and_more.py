# Generated by Django 4.2.6 on 2024-04-02 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_order_accessory_order_payment_datetime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='accessory',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('accessory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.accessory')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.order')),
            ],
        ),
    ]