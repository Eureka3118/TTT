# Generated by Django 5.1.2 on 2024-10-22 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_tag_remove_post_updated_at_post_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default='Default comment text'),
            preserve_default=False,
        ),
    ]
