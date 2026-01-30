from django.shortcuts import render
from django.http import HttpResponse
from .models import Grocery


def home(request):
    return render(request, "home.html")


def guide(request):
    return render(request, "guide.html")


def grocery_index(request):
    groceries = Grocery.objects.all()
    return render(request, "groceries/index.html", {"groceries": groceries})



