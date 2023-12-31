# Generated by Django 5.0 on 2023-12-13 00:05

import django.core.validators
import post.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_tag_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='icons/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png']), post.models.validate_file_size]),
        ),
    ]
