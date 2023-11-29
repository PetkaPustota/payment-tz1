from django.db import models
from django.db.models import Sum


# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return self.name
