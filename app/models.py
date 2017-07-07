from __future__ import unicode_literals

from django.db import models

# Create your models here.
class itemDataPoint(models.Model):
    itemID=models.IntegerField()
    date=models.DateTimeField()
    price=models.IntegerField()
    