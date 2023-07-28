from django.db import models

from framework.authentication.models import Role


# 菜单
class Menu(models.Model):
    # 菜单名
    name = models.CharField(max_length=32, null=False)
    # 父级菜单
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=False)
    # 页面类型
    page_type = models.IntegerField(null=False)  # 1-主目录/模块 2-路由
    # 菜单类型
    menu_type = models.IntegerField(null=False)  # 1-用户页面 2-系统管理 3-安全管理 4-审计管理 5-运维管理
    # 授权类型
    auth_type = models.IntegerField(null=False)  # 1-公开 2-角色授权 3-用户登录
    # 路由路径
    path = models.CharField(max_length=255, null=False)
    # 页面路径
    component = models.CharField(max_length=255, null=False)
    # 图标
    icon = models.CharField(max_length=255, null=False)
    # 是否启用
    enable = models.BooleanField(default=True)
    # 排序
    sort = models.IntegerField(default=0)
    # 分配给角色
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role_menus', null=True, blank=True)
    # 创建人
    create_user = models.CharField(max_length=32, null=False)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 修改人
    update_user = models.CharField(max_length=32, null=False)
    # 修改时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ddb_menu'
        ordering = ['id']
