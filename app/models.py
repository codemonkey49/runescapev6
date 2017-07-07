from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class itemDataPoint(models.Model):
    id = models.BigIntegerField(primary_key = True)
    itemID=models.IntegerField(default=0)
    date=models.DateTimeField(default=timezone.now())
    price=models.IntegerField(default=0)
    