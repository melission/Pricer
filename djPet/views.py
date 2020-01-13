from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    # home_page_title = 'Request was formatted with .format method'
    return render(request, "home_page.html", {'title': 'this is really THE home page'})


def contact_page(request):
    return render(request, 'contacts.html', {'title': 'All sort of links'})


def about_page(request):
    about_page_title = "Hey, i'm here to tell you about me"
    return render(request, 'home_page.html', {'title': about_page_title})
