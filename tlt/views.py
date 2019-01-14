from django.shortcuts import render
from .forms import SubscriberForm

def index(request):
    name = "Konstantin"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()
    return render(request, 'templatesGpteTlt/index.html', locals())


def purchases(request):
    return render(request, 'templatesGpteTlt/purchases.html', locals())

def debt(request):
    return render(request, 'templatesGpteTlt/debt.html', locals())

def conctacts(request):
    return render(request, 'templatesGpteTlt/contacts.html', locals())

def tariff(request):
    return render(request, 'templatesGpteTlt/tariff.html', locals())
