# Generated by Django 5.0.1 on 2024-01-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_users_contactno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='contactNo',
            field=models.BigIntegerField(max_length=10),
        ),
    ]
