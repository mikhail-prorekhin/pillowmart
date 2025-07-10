from django.shortcuts import render
from products.models import Categories, Products


def index(request):

    products = Products.objects.all().order_by("-id")
    context = {
        "title": "product list",
        "products": products,
        # {
        #     "id": 20,
        #     "title": "Anti-Snore Pillow",
        #     "description": "Specially designed to reduce snoring",
        #     "price": 69.99,
        #     "image": "img/product/product_list_10.png",
        # },
        "categories": Categories.objects.all(),
    }
    return render(request, "products/catalog.html", context)


def product(request):
    context = {
        "title": "Product details",
    }
    return render(request, "products/catalog.html", context)
