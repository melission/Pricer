from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.files import File
from .forms import PricerForm
from .calculations import pricesCollector
from django.core.files.storage import FileSystemStorage



def home_page(request):
    # home_page_title = 'Request was formatted with .format method'
    return render(request, "home_page.html", {'title': 'this is really THE home page'})


def contact_page(request):
    return render(request, 'contacts.html', {'title': 'All sort of links'})


# def pricer_page(request):
#     """"""
#     print('request Post before everything: ', request.POST, request.FILES)
#     print('request without .POST', request)
#     if request.method == "POST":
#     # if request.method == "POST" and request.FILES['fileWithPrices']:
#         print('within IF and AND loop')
#
#         # print('after .Model definition ', form, pricer.document, 'shopID', pricer.shopID)
#         form = PricerForm(request.POST)
#         print('after form=pricerform()')
#         if form.is_valid():
#             print('inside if form is valid')
#             # form.save()
#             cleanedForm = form.cleaned_data
#             print(cleanedForm, cleanedForm['shopID'])
#         # if request.FILES:
#         #     print('within request.Files')
#         #     PriceChanger(request.FILES['file'])
#         print('before definition of the form')
#         # neededColumns = columnIndex(request.POST)
#         # print(neededColumns)
#         # pricer(document=request.FILES, shopID=neededColumns[0], name=neededColumns[1],
#         #        amount=neededColumns[2], price=neededColumns[3], partNumber=neededColumns[4],
#         #        MRP=neededColumns[5])
#         # print('Form before isvalid: ', form)
#         # if form.is_valid():
#         #     print(form.cleaned_data)
#         #     return render(request, 'pricer.html')
#         # else:
#         #     print('Wrong')
#         #     return render(request, 'pricer.html')
#         return render(request, 'pricer.html')
#     return render(request, 'pricer.html')



def new_pricer_page(request):
    template = "pricer.html"
    if request.method == "POST":
        form = PricerForm(request.POST)
        uploaded_file = request.FILES['document']
        # print(form)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        print(uploaded_file.size)
        print(uploaded_file.content_type)
        if form.is_valid():
            print('inside if form is valid')
            cleanedData = form.cleaned_data
            neededColumns = []
            for i in cleanedData.values():
                neededColumns.append(i)
            print(neededColumns)
            # file = File
            # ready_to_use_prices = pricesCollector(neededColumns, file)
            # return
        else:
            template = 'pricer.html'
            return render(request, template)
        print('after if loop, neededColumns: ', neededColumns)
    # https://docs.djangoproject.com/en/3.0/ref/contrib/messages/
    return render(request, template)


def about_page(request):
    about_page_title = "Hey, i'm here to tell you about me"
    return render(request, 'home_page.html', {'title': about_page_title})


def easter_egg_page(request):
    print('before render, request: ', request)
    easter_egg_title = 'Wow, nice to see you here!'
    form = PricerForm()
    print(form)
    template = 'easter_egg.html'
    context = {
        "form": form
    }
    return render(request, template, context)

# def page_not_found(request, exception):
#     return render(request, '404.html', {'title': 'Sorry, looks like we are lost'})
#
#
# def error_500(request):
#     return render(request, '404.html', )

