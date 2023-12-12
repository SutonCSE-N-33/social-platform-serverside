# Generated by Django 4.2.4 on 2023-11-23 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('react', '0001_initial'),
        ('comment', '0004_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.comment'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='react',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='react.react'),
        ),
    ]
