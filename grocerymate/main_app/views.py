from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Grocery, Coupon
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import BoughtForm

def home(request):
    return render(request, "home.html")


def guide(request):
    return render(request, "guide.html")


def groceries_index(request):
    groceries = Grocery.objects.all()
    return render(request, "groceries/index.html", {"groceries": groceries})


def groceries_detail(request, grocery_id):
    grocery = Grocery.objects.get(id=grocery_id)
    bought_form = BoughtForm()
    return render(request, "groceries/detail.html", {
        "grocery": grocery,
        'bought_form': bought_form
        })

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

def add_bought(request, grocery_id):
    form= BoughtForm(request.POST)
    if form.is_valid():
        new_bought = form.save(commit=False)
        new_bought.grocery_id = grocery_id
        new_bought.save()
    return redirect('detail', grocery_id=grocery_id)

