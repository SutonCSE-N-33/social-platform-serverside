# Generated by Django 4.2.4 on 2023-12-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0006_delete_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='profile_avatar',
            field=models.URLField(blank=True, null=True),
        ),
    ]
