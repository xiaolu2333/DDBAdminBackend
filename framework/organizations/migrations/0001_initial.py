# Generated by Django 4.1.7 on 2023-04-12 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('parent_code', models.CharField(max_length=255, null=True)),
                ('enabled', models.BooleanField(default=True)),
                ('sort_number', models.IntegerField(default=0)),
                ('level', models.CharField(max_length=255)),
                ('org_desc', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'ddb_organization',
                'ordering': ['id'],
            },
        ),
    ]
