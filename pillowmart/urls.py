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
from django.contrib import admin
from django.urls import path
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='index'),
    path('about/', main_views.about, name='about'),
    
#     path('contacts/', main_views.contacts, name='contacts'),
#     path('products/', main_views.products, name='products'),
#     path('products/<int:product_id>/', main_views.product_detail, name='product
# _detail'),
#     path('cart/', main_views.cart, name='cart'),
#     path('checkout/', main_views.checkout, name='checkout'),
#     path('order_success/', main_views.order_success, name='order_success'),
#     path('search/', main_views.search, name='search'),
#     path('profile/', main_views.profile, name='profile'),
#     path('profile/edit/', main_views.edit_profile, name='edit_profile'),
#     path('profile/orders/', main_views.order_history, name='order_history'),
#     path('profile/orders/<int:order_id>/', main_views.order_detail, name='order_detail'),
#     path('profile/wishlist/', main_views.wishlist, name='wishlist'),
#     path('profile/wishlist/add/<int:product_id>/', main_views.add_to_wishlist, name='add_to_wishlist'),
#     path('profile/wishlist/remove/<int:product
]
