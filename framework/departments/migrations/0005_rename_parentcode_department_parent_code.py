# Generated by Django 4.1.7 on 2023-05-29 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0004_department_create_time_department_update_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='parentCode',
            new_name='parent_code',
        ),
    ]