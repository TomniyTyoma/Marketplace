from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Product


def checkout(request):
    return render(request, 'store/checkout.html', {})


def blank(request):
    return render(request, 'store/cart.html', {})


def product(request):
    return render(request, 'store/product.html', {})


class ProductsListView(ListView):
    model = Product
    template_name = 'store.html'
