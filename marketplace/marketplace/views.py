from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def store(request):
    return render(request, 'store.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})

def blank(request):
    return render(request, 'blank.html', {})

def product(request):
    return render(request, 'product.html', {})