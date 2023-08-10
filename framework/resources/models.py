from django.db import models

from framework.authentication.models import Role


# 菜单
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    # 菜单名
    name = models.CharField(max_length=32, null=False)
    # 父级菜单
    parent_id = models.IntegerField(null=False, default=0)
    # 页面类型
    page_type = models.IntegerField(null=False)  # 1-主目录/模块 2-路由
    # 菜单类型
    menu_type = models.IntegerField(null=False)  # 1-用户页面 2-系统管理 3-安全管理 4-审计管理 5-运维管理
    # 授权类型
    auth_type = models.IntegerField(null=False)  # 1-公开 2-授权
    # 路由路径
    path = models.CharField(max_length=255, null=False)
    # 页面路径
    component = models.CharField(max_length=255, null=False)
    # 图标
    icon = models.CharField(max_length=255, null=True)
    # 是否启用
    enable = models.BooleanField(default=True)
    # 是否隐藏
    hidden = models.BooleanField(default=False)
    # 排序
    sort = models.IntegerField(default=0, null=False)
    # 分配给角色
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role_menus', null=True, blank=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 修改时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ddb_menu'
        ordering = ['id']
