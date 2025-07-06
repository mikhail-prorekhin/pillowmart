from django.http import HttpResponse
from django.shortcuts import render


def index(request, page_title="Home 11", show_sidebar=True) :
    context = {
        'title': page_title,
        'show_sidebar': show_sidebar
    }
    return render(request, 'main/index.html', context)


def about(request, company_name="Our Company", year_founded=2000) :
    """
    Render the about page.
    """
    context = {
        'company_name': company_name,
        'year_founded': year_founded
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
   

# def about(request) :
#     """
#     Render the about page.
#     """
#     # return render(request, 'main/about.html')
#     return HttpResponse('About us page')


# def contacts(request) :
#     """    Render the contacts page.
#     """
#     return render(request, 'main/contacts.html')  

