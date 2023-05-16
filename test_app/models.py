from django.db import models


# Create your models here.
class TestData(models.Model):
    # id 为自增字段
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.IntegerField()

    class Meta:
        db_table = 'test_data'

    def __str__(self):
        return self.name
