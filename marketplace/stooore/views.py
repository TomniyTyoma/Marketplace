from django.shortcuts import render, redirect


def checkout(request):
    return render(request, 'store/checkout.html', {})


def blank(request):
    return render(request, 'store/blank.html', {})


def product(request):
    return render(request, 'store/product.html', {})


def store(request):
    return render(request, 'store.html', {})
