# Generated by Django 4.1.7 on 2023-07-28 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=32)),
                ('page_type', models.IntegerField()),
                ('menu_type', models.IntegerField()),
                ('auth_type', models.IntegerField()),
                ('path', models.CharField(max_length=255)),
                ('component_path', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
                ('enable', models.BooleanField(default=True)),
                ('sort', models.IntegerField(default=0)),
                ('component', models.CharField(max_length=255)),
                ('create_user', models.CharField(max_length=32)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_user', models.CharField(max_length=32)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.menu')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role_menus', to='authentication.role')),
            ],
            options={
                'db_table': 'ddb_menu',
                'ordering': ['id'],
            },
        ),
    ]
