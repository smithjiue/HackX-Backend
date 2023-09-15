from django.db import models
from datetime import date
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    qty = models.IntegerField(default=1)
    price = models.IntegerField(default=100)
    expiry = models.BooleanField(default=False)
    if expiry:
        expiry_date = models.DateField(default=date.today)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    