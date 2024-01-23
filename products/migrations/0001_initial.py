# Generated by Django 5.0.1 on 2024-01-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.URLField(max_length=1000)),
                ('category', models.CharField(choices=[('electronics', 'electronics'), ('books', 'Books'), ('watches', 'Watches')], max_length=100)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
    ]
