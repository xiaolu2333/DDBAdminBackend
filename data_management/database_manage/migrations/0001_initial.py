# Generated by Django 4.1.7 on 2023-06-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='数据库名称')),
                ('type', models.IntegerField(verbose_name='数据库类型')),
                ('ip', models.CharField(max_length=255, verbose_name='数据库IP')),
                ('port', models.CharField(max_length=255, verbose_name='数据库端口')),
                ('username', models.CharField(max_length=255, verbose_name='数据库用户名')),
                ('password', models.CharField(max_length=255, verbose_name='数据库密码')),
                ('is_published', models.BooleanField(default=False, verbose_name='是否发布')),
                ('register_status', models.CharField(max_length=255, verbose_name='注册状态')),
                ('creator', models.CharField(max_length=255, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
    ]
