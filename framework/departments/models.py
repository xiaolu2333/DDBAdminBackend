from django.db import models

from framework.organizations.models import Organization


class Department(models.Model):
    name = models.CharField("部门名称", max_length=255)
    code = models.CharField("部门代码", max_length=255)
    parentCode = models.CharField("上级部门", max_length=255)
    enabled = models.BooleanField("启用")
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
