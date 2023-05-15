from django.db import models

from framework.organizations.models import Organization
from framework.departments.models import Department


# 用户
class DDBAdminUser(models.Model):
    # 用户ID
    id = models.AutoField(primary_key=True)
    # 用户名
    user_name = models.CharField(max_length=255)
    # 用户编码
    user_code = models.CharField(max_length=255)
    # 用户密码
    password = models.CharField(max_length=255)
    # 用户密级
    secret_level = models.CharField(max_length=255)
    # # 用户所属机构
    # org = models.ForeignKey('Organization', on_delete=models.CASCADE)
    # # 用户所属部门
    # dept = models.ForeignKey('Department', on_delete=models.CASCADE)
    # # 用户所属角色
    # role = models.ForeignKey('DDBAdminRole', on_delete=models.CASCADE)
    # 是否启用
    enabled = models.BooleanField(default=True)
    # 是否锁定
    locked = models.BooleanField(default=False)
    # 锁定时间
    unLock_time = models.DateTimeField()
    # 登录IP历史
    login_history = models.CharField(max_length=2550)
    # 密码过期日期
    passExpireDate = models.DateTimeField()
    # 密码修改日期
    passChangeDate = models.DateTimeField()
    # 排序号
    sortNum = models.IntegerField()
    # 备注
    remark = models.TextField()
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['id']


# 角色
class DDBAdminRole:
    ROLE = (
        (1, '安全管理员'),
        (2, '安全审计员'),
        (3, '安全保密员'),
        (4, '普通用户'),
    )

    # 角色ID
    id = models.AutoField(primary_key=True)
    # 角色名
    name = models.CharField(choices=ROLE)
    # 菜单权限
    menu = models.CharField(max_length=32)
    # 按钮权限
    button = models.CharField(max_length=32)
    # 角色描述
    desc = models.CharField(max_length=255)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
