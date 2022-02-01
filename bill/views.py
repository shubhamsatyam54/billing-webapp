from django.shortcuts import render
from .models import Stock, Party, Product, Batch


def dashboard(request):
    return render(request, "dashboard.html")


def stock(request):
    st = Stock.objects.all()
    return render(request, "Stock.html", {'st': st})


def saleshistory(request):
    return render(request, "saleshistory.html")


def newsale(request):
    party = Party.objects.all()
    product = Product.objects.all()
    
    return render(request, "newsale.html", {'Party': party})


def purchasehistory(request):
    return render(request, "purchasehistory.html")


def newpurchase(request):
    return render(request, "newpurchase.html")


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}

    return render(request, 'error_404.html', data)
