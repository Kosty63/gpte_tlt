from django.db import models

class IndicationsModel(models.Model):
    ls = models.BigIntegerField()
    fullName = models.CharField(max_length=256)
    address = models.CharField(max_length=1000)
    periud = models.CharField(max_length=256)
    firstCount = models.IntegerField()
    twoCount = models.IntegerField(blank=True, null=True)
    freeCount = models.IntegerField(blank=True, null=True)
    forCount = models.IntegerField(blank=True, null=True)
