from django.db import models

# Create your models here.
# 菜单
class DDBAdminMenu(models.Model):
    # 菜单名
    name = models.CharField(max_length=32)
    # 菜单链接
    url = models.CharField(max_length=32)
    # 父级菜单
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    # 是否显示
    is_show = models.BooleanField(default=True)
    # 排序
    sort = models.IntegerField(default=0)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ddb_admin_menu'
        ordering = ['id']
