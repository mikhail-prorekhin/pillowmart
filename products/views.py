from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, render
from django.template.loader import render_to_string
from products.models import Categories, Products


def catalog(request, category_slug=None):
    print("Category slug:", category_slug)
    if category_slug == None:
        products = Products.objects.all().order_by("-id")
    else:
        products = get_list_or_404(
            Products.objects.filter(category__slug=category_slug)
        )

    paginator = Paginator(products, 10)
    current_page = paginator.page(1)

    context = {
        "title": "product list",
        "products": current_page,
    }
    return render(request, "products/catalog.html", context)


def load_more_products(request, category_slug=None):
    page = int(request.GET.get("page", 1))

    products = Products.objects.all().order_by("-id")

    paginator = Paginator(products, 10)
    current_page = paginator.page(page)

    html = render_to_string("products/product_list.html", {"products": current_page})
    return JsonResponse(
        {
            "html": html,
            "next": (
                paginator.get_page(page + 1).number
                if paginator.num_pages > page
                else None
            ),
        }
    )


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        "title": product.name,
        "product": product,
        "images": (
            product.big_image_1,
            product.big_image_2,
            product.big_image_3,
        ),
    }
    return render(request, "products/product.html", context)
