from django.shortcuts import render
from django.http import HttpResponse
from .models import Grocery
from django.views.generic.edit import CreateView, DeleteView, UpdateView

def home(request):
    return render(request, "home.html")


def guide(request):
    return render(request, "guide.html")


def groceries_index(request):
    groceries = Grocery.objects.all()
    return render(request, "groceries/index.html", {"groceries": groceries})


def groceries_detail(request, grocery_id):
    grocery = Grocery.objects.get(id=grocery_id)
    return render(request, "groceries/detail.html", {"grocery": grocery })

class GroceryCreate(CreateView):
    model = Grocery
    fields = '__all__'
    success_url = '/groceries/'

class GroceryUpdate(UpdateView):
    model = Grocery
    fields = '__all__'

class GroceryDelete(DeleteView):
    model = Grocery
    success_url = '/groceries/'
