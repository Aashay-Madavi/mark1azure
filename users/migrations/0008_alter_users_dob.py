# Generated by Django 5.0.1 on 2024-01-25 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_users_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]