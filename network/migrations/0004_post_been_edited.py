# Generated by Django 3.2.12 on 2025-04-08 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='been_edited',
            field=models.BooleanField(default=False),
        ),
    ]
