from django.http import HttpResponse
from django.shortcuts import render


def index(request) :
    context = {
        'title': "Home",
    }
    return render(request, 'main/index.html', context)


def about(request) :
    context = {
        'title': "About",
    }
    return render(request, 'main/about.html', context)


# def contacts(request, department="General", email="contact@example.com") :
#     """
#     Render the contacts page.
#     """
#     context = {
#         'department': department,
#         'email': email
#     }
#     return render(request, 'main/contacts.html', context)    return render(request, 'main/index.html', context)
   


# def contacts(request) :
#     """    Render the contacts page.
#     """
#     return render(request, 'main/contacts.html')  

