from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='main_app/static/uploads/', default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'grocery_id': self.id})

