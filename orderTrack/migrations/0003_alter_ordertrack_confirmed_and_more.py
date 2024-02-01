# Generated by Django 5.0.1 on 2024-02-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderTrack', '0002_alter_ordertrack_confirmed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertrack',
            name='confirmed',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='ordertrack',
            name='dispatched',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='ordertrack',
            name='in_transit',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='ordertrack',
            name='out_for_delivery',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='ordertrack',
            name='shipped',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
