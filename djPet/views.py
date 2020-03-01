from django.http import HttpResponse, Http404
from django.shortcuts import render
from .forms import PriceChanger

def home_page(request):
    # home_page_title = 'Request was formatted with .format method'
    return render(request, "home_page.html", {'title': 'this is really THE home page'})


def contact_page(request):
    return render(request, 'contacts.html', {'title': 'All sort of links'})


def pricer_page(request):
    # print(request.POST)
    if request.method == 'POST':
        form = PriceChanger(request.POST)
        print(form)
        if form.is_valid():
            print(form.creaned_data)
            return render(request, 'pricer.html')
        else:
            print('Wrong')
            return render(request, 'pricer.html')

    return render(request, 'pricer.html')

def about_page(request):
    about_page_title = "Hey, i'm here to tell you about me"
    return render(request, 'home_page.html', {'title': about_page_title})


# def page_not_found(request, exception):
#     return render(request, '404.html', {'title': 'Sorry, looks like we are lost'})
#
#
# def error_500(request):
#     return render(request, '404.html', )

