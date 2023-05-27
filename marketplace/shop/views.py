from django.shortcuts import render
from django.views.generic import ListView

from stooore.models import Product


class ProductsListView(ListView):
    model = Product
    template_name = 'home.html'
