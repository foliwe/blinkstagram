# Generated by Django 5.0 on 2023-12-12 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_tag_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='icons/'),
        ),
    ]
