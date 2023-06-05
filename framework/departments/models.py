from django.db import models

from framework.organizations.models import Organization


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("部门名称", max_length=255)
    code = models.CharField("部门代码", max_length=255)
    parent_code = models.CharField("上级部门", max_length=255)
    enabled = models.BooleanField("启用")
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ddb_department'
        ordering = ['id']
