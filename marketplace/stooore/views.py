from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView

from .models import Product


def checkout(request):
    return render(request, 'store/checkout.html', {})


def blank(request):
    return render(request, 'store/cart.html', {})


class ProductsListView(ListView):
    model = Product
    template_name = 'store.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'

