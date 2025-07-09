from django.shortcuts import render
from products.models import Categories


def index(request):

    context = {
        "title": "product list",
        "products": (
            {
                "id": 1,
                "title": "Classic Memory Foam Pillow",
                "description": "Ergonomic memory foam pillow for optimal neck support",
                "price": 49.99,
                "image": "img/product/product_list_1.png",
            },
            {
                "id": 2,
                "title": "Decorative Throw Pillow",
                "description": "Stylish accent pillow with modern geometric pattern",
                "price": 29.99,
                "image": "img/product/product_list_2.png",
            },
            {
                "id": 3,
                "title": "Cooling Gel Pillow",
                "description": "Temperature-regulating pillow for hot sleepers",
                "price": 59.99,
                "image": "img/product/product_list_3.png",
            },
            {
                "id": 4,
                "title": "Body Pillow",
                "description": "Full-length body pillow for side sleepers",
                "price": 69.99,
                "image": "img/product/product_list_4.png",
            },
            {
                "id": 5,
                "title": "Cervical Support Pillow",
                "description": "Therapeutic pillow designed for neck pain relief",
                "price": 79.99,
                "image": "img/product/product_list_5.png",
            },
            {
                "id": 6,
                "title": "Bamboo Pillow",
                "description": "Eco-friendly bamboo cover with adjustable fill",
                "price": 54.99,
                "image": "img/product/product_list_6.png",
            },
            {
                "id": 7,
                "title": "Kids Character Pillow",
                "description": "Fun and colorful pillow for children",
                "price": 24.99,
                "image": "img/product/product_list_7.png",
            },
            {
                "id": 8,
                "title": "Travel Neck Pillow",
                "description": "Compact and comfortable travel companion",
                "price": 19.99,
                "image": "img/product/product_list_8.png",
            },
            {
                "id": 9,
                "title": "Wedge Pillow",
                "description": "Supportive pillow for reading and relaxing in bed",
                "price": 44.99,
                "image": "img/product/product_list_9.png",
            },
            {
                "id": 10,
                "title": "Orthopedic Pillow",
                "description": "Medical-grade support for back and spine alignment",
                "price": 89.99,
                "image": "img/product/product_list_10.png",
            },
            {
                "id": 11,
                "title": "Silk Pillowcase Set",
                "description": "Luxury silk pillowcase for hair and skin care",
                "price": 39.99,
                "image": "img/product/product_list_1.png",
            },
            {
                "id": 12,
                "title": "Floor Cushion",
                "description": "Large decorative floor pillow for casual seating",
                "price": 49.99,
                "image": "img/product/product_list_2.png",
            },
            {
                "id": 13,
                "title": "Pregnancy Pillow",
                "description": "Full body support pillow for expecting mothers",
                "price": 84.99,
                "image": "img/product/product_list_3.png",
            },
            {
                "id": 14,
                "title": "Outdoor Patio Pillow",
                "description": "Weather-resistant pillow for outdoor furniture",
                "price": 34.99,
                "image": "img/product/product_list_4.png",
            },
            {
                "id": 15,
                "title": "Meditation Cushion",
                "description": "Traditional zafu pillow for meditation practice",
                "price": 45.99,
                "image": "img/product/product_list_5.png",
            },
            {
                "id": 16,
                "title": "Pet Bed Pillow",
                "description": "Cozy pillow bed for cats and small dogs",
                "price": 29.99,
                "image": "img/product/product_list_6.png",
            },
            {
                "id": 17,
                "title": "Lumbar Support Pillow",
                "description": "Office chair back support cushion",
                "price": 39.99,
                "image": "img/product/product_list_7.png",
            },
            {
                "id": 18,
                "title": "Buckwheat Hull Pillow",
                "description": "Traditional Asian-style pillow for firm support",
                "price": 64.99,
                "image": "img/product/product_list_8.png",
            },
            {
                "id": 19,
                "title": "Aromatherapy Pillow",
                "description": "Lavender-infused pillow for relaxation",
                "price": 49.99,
                "image": "img/product/product_list_9.png",
            },
            {
                "id": 20,
                "title": "Anti-Snore Pillow",
                "description": "Specially designed to reduce snoring",
                "price": 69.99,
                "image": "img/product/product_list_10.png",
            },
        ),
        "categories": Categories.objects.all(),
    }
    return render(request, "products/catalog.html", context)


def product(request):
    context = {
        "title": "Product details",
    }
    return render(request, "products/catalog.html", context)
