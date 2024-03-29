# Generated by Django 5.0.1 on 2024-01-22 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('pen', 'Pending'), ('can', 'Cancled'), ('del', 'Delivered')], max_length=100)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]