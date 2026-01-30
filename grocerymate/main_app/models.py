from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.name


