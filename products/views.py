from django.shortcuts import render
from products.models import Categories, Products


def index(request):

    products = Products.objects.all().order_by("-id")
    context = {
        "title": "product list",
        "products": products,
    }
    return render(request, "products/catalog.html", context)


def product(request):
    context = {
        "title": "Product details",
    }
    return render(request, "products/catalog.html", context)
