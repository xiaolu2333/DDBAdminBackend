# Generated by Django 4.1.7 on 2023-08-10 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_menu_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
