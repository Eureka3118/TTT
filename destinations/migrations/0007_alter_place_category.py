# Generated by Django 5.1.2 on 2024-11-26 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0006_alter_category_options_alter_place_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='destinations.category'),
        ),
    ]
