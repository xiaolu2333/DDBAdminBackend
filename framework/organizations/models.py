from django.db import models


class Organization(models.Model):
    # 机构ID
    id = models.AutoField(primary_key=True)
    # 机构名称
    name = models.CharField(max_length=255, unique=True, null=False)
    # 机构代码
    code = models.CharField(max_length=255, unique=True, null=False)
    # 父级机构代码
    parent_code = models.CharField(max_length=255, null=True)
    # 是否启用
    enabled = models.BooleanField(default=True)
    # 排序号
    sort_number = models.IntegerField(default=0)
    # 机构层级
    level = models.CharField(max_length=255)
    # 机构描述
    org_desc = models.TextField()
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ddb_organization'
        ordering = ['id']
