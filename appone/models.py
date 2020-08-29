from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    qty = models.IntegerField()
    price = models.FloatField()
    remark = models.TextField(max_length=100)
    active = models.CharField(max_length=3,default='Y')

