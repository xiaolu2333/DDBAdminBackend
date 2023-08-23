from django.db import models

from framework.organizations.models import Organization
from framework.departments.models import Department
from django.contrib.auth.models import AbstractUser


# 角色
class Role(models.Model):
    # 角色ID
    id = models.AutoField(primary_key=True)
    # 角色类型
    type = models.IntegerField(null=False)  # 1-管理角色 2-业务角色 3-普通角色
    # 角色名
    name = models.CharField(max_length=255)
    # 角色编码
    code = models.CharField(max_length=255)
    # 是否启用
    enabled = models.BooleanField(default=True)
    # 排序
    sort = models.IntegerField(default=0)
    # 角色描述
    desc = models.TextField()
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ddb_role'
        ordering = ['id']


# 用户
class User(models.Model):
    # 用户ID
    id = models.AutoField(primary_key=True)
    # 用户名
    username = models.CharField(max_length=255)
    # 用户密码
    password = models.CharField(max_length=255)
    # 用户所属部门
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    # 用户角色
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    # 是否启用
    enabled = models.BooleanField(default=True)
    # 用户描述
    desc = models.TextField()
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ddb_user'
        ordering = ['id']
