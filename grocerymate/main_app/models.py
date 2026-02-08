from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Coupon(models.Model):
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse("coupons_detail", kwargs={"pk": self.id})

class Grocery(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='main_app/static/uploads/', default='')
    coupons = models.ManyToManyField(Coupon)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'grocery_id': self.id})

class Bought(models.Model):
    date = models.DateField()
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.Grocery} bought on {self.date}"
