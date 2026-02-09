from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Grocery, Coupon
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .forms import BoughtForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, "home.html")


def guide(request):
    return render(request, "guide.html")

@login_required
def groceries_index(request):
    groceries = Grocery.objects.filter(user=request.user)
    return render(request, "groceries/index.html", {"groceries": groceries})

@login_required
def groceries_detail(request, grocery_id):
    grocery = Grocery.objects.get(id=grocery_id)
    bought_form = BoughtForm()
    unadded_coupons = Coupon.objects.exclude(
        id__in=grocery.coupons.all().values_list("id")
    )
    return render(
        request,
        "groceries/detail.html",
        {"grocery": grocery, "bought_form": bought_form, "coupons": unadded_coupons},
    )


class GroceryCreate(LoginRequiredMixin, CreateView):
    model = Grocery
    fields = ["name", "brand", "image"]
    success_url = "/groceries/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GroceryUpdate(LoginRequiredMixin, UpdateView):
    model = Grocery
    fields = "__all__"


class GroceryDelete(LoginRequiredMixin, DeleteView):
    model = Grocery
    success_url = "/groceries/"


@login_required
def add_bought(request, grocery_id):
    form = BoughtForm(request.POST)
    if form.is_valid():
        new_bought = form.save(commit=False)
        new_bought.grocery_id = grocery_id
        new_bought.save()
    return redirect("detail", grocery_id=grocery_id)

@login_required
def apply_coupon(request, grocery_id, coupon_id):
    Grocery.objects.get(id=grocery_id).coupons.add(coupon_id)
    return redirect("detail", grocery_id=grocery_id)

@login_required
def unapply_coupon(request, grocery_id, coupon_id):
    Grocery.objects.get(id=grocery_id).coupons.remove(coupon_id)
    return redirect("detail", grocery_id=grocery_id)


class CouponList(LoginRequiredMixin, ListView):
    model = Coupon


class CouponDetail(LoginRequiredMixin, DetailView):
    model = Coupon


class CouponCreate(LoginRequiredMixin, CreateView):
    model = Coupon
    fields = "__all__"


class CouponUpdate(LoginRequiredMixin, UpdateView):
    model = Coupon
    fields = "__all__"


class CouponDelete(LoginRequiredMixin, DeleteView):
    model = Coupon
    success_url = "/coupons/"

@login_required
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
