# Generated by Django 4.1.7 on 2023-05-16 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'test_data',
            },
        ),
    ]