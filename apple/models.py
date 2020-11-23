from django.db import models
from django.utils.timezone import now

# Create your models here.

class applesTable1(models.Model):
    node_id = models.CharField(max_length=64)
    abs_diff_angle = models.FloatField(blank=True, null=True)
    is_geometry_unreasonable = models.IntegerField(blank=True, null=True)
    data_version = models.DateField(blank=True, null=True, default=now)
    insert_time = models.DateTimeField(blank=True, null=True, default=now)

    class Meta:
        managed = False
        db_table = 'apples_table1'