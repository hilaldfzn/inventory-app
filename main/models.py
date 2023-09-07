from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.BigIntegerField()
    power = models.IntegerField()
    category = models.CharField(max_length=255)