# Generated by Django 5.0 on 2023-12-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_tag_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='tag',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
