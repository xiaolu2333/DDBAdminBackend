from django.db import models


class DataTreeNode(models.Model):
    """
    数据树节点
    """
    oid = models.AutoField(primary_key=True)
    # 节点类型
    node_type = models.CharField(max_length=100, null=False, blank=False)
    # 节点名称
    name = models.CharField(max_length=100, null=False, blank=False)
    # 父节点编码
    parent_oid = models.IntegerField(null=False, blank=False)

    class Meta:
        # 指定表名
        db_table = 'data_tree_node'
        # 指定排序方式
        ordering = ['oid']

    def __str__(self):
        return self.node_type + ' - ' + self.name
