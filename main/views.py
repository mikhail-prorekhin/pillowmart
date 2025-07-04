from django.http import HttpResponse
from django.shortcuts import render


def index(request) :
    """
    Render the index page.
    """
    # return render(request, 'main/index.html')
    return HttpResponse('Hello, world!')

def about(request) :
    """
    Render the about page.
    """
    # return render(request, 'main/about.html')
    return HttpResponse('About us page')


# def contacts(request) :
#     """    Render the contacts page.
#     """
#     return render(request, 'main/contacts.html')  

