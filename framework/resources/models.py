from django.db import models

from framework.authentication.models import Role


# 菜单
class Menu(models.Model):
    # 菜单名
    name = models.CharField(max_length=32, null=False)
    # 菜单链接
    url = models.CharField(max_length=32, null=False)
    # 父级菜单
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=False)
    # 是否显示
    is_show = models.BooleanField(default=True)
    # 排序
    sort = models.IntegerField(default=0)
    # 菜单组件
    component = models.CharField(max_length=255, null=False)
    # 分配给角色
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role_menus', null=False)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ddb_menu'
        ordering = ['id']
