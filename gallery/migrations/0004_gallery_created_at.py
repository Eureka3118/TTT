# Generated by Django 5.1.2 on 2024-10-27 07:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_alter_image_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='created_at',
            field=models.ImageField(upload_to='gallery_images/'),
            
            preserve_default=False,
        ),
    ]
