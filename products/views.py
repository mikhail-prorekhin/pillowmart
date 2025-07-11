from django.shortcuts import get_list_or_404, render
from products.models import Categories, Products


def catalog(request, category_slug=None):
    print("Category slug:", category_slug)
    if category_slug == None:
        products = Products.objects.all().order_by("-id")
    else:
        products = get_list_or_404(
            Products.objects.filter(category__slug=category_slug)
        )

    context = {
        "title": "product list",
        "products": products,
    }
    return render(request, "products/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        "title": "Product details",
        "product": product,
        "images": (
            product.big_image_1,
            product.big_image_2,
            product.big_image_3,
        ),
    }
    return render(request, "products/product.html", context)
