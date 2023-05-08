from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def store(request):
    return render(request, 'store.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})


