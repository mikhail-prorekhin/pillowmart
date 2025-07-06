from django.shortcuts import render


def index(request) :
    context = {
        'title': "Home",
    }
    return render(request, 'products/catalog.html', context)


def product(request) :
    context = {
        'title': "About",
    }
    return render(request, 'products/product.html', context)

