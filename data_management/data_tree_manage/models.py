from django.db import models


class DataTreeNode(models.Model):
    """
    数据树节点
    """
    # 服务器组名称
    server_group_name = models.CharField(max_length=100, null=False, blank=False)
    # 服务器名称
    server_name = models.CharField(max_length=100, null=True, blank=True)
    # 数据库名称
    db_name = models.CharField(max_length=100, null=True, blank=True)
    # 节点类型
    node_type = models.CharField(max_length=100, null=False, blank=False)
    # 节点名称
    name = models.CharField(max_length=100, null=False, blank=False)
    # 节点编码
    code = models.CharField(max_length=100, null=True, blank=True)
    # 父节点编码
    parent_code = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        # 指定表名
        db_table = 'data_tree_node'
        # 指定排序方式
        ordering = ['id']

    def __str__(self):
        return self.node_type + ' - ' + self.name
