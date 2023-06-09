# Generated by Django 4.1.7 on 2023-05-29 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_alter_department_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
