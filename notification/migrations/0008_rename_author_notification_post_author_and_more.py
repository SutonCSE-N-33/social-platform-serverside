# Generated by Django 4.2.4 on 2023-12-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0007_notification_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='author',
            new_name='post_author',
        ),
        migrations.AddField(
            model_name='countnotification',
            name='post_author',
            field=models.IntegerField(null=True),
        ),
    ]