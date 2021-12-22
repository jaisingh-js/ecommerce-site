from django.shortcuts import render

# Create your views here.

def store(request):
    context = {}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def catalogue(request):
    context = {}
    return render(request, 'store/catalogue.html', context)