from django.db import models


class Department(models.Model):
    name = models.CharField("部门名称", max_length=255)
    code = models.CharField("部门代码", max_length=255)
    parentCode = models.CharField("上级部门", max_length=255)
    deptLevel = models.CharField("部门级别", max_length=255)
    deptDesc = models.TextField("部门描述")
    levelDesc = models.TextField("机构层级描述")
    enabled = models.BooleanField("启用")
    sortNum = models.IntegerField("排序")
    orgCode = models.CharField("所属机构", max_length=255)
    remark = models.TextField("备注")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
