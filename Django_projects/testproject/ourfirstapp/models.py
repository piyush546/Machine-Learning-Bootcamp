from django.db import models

# Create your models here.
class TestTable2(models.Model):
    create_date = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length =1000, null=False)
