"""
URL configuration for pillowmart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from products import views

app_name = "products"

urlpatterns = [
    path("product/<slug:product_slug>/", views.product, name="product"),
    path(
        "load_more_products/",
        views.load_more_products,
        name="paginator",
    ),
    path(
        "<slug:category_slug>/load_more_products/",
        views.load_more_products,
        name="paginator",
    ),
    path("<slug:category_slug>/", views.catalog, name="index"),
    path("", views.catalog, name="index"),
]
