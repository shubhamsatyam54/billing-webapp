from django.shortcuts import render

def dashboard(request):
    return render(request, "dashboard.html")

def stock(request):
    return render(request, "Stock.html")

def saleshistory(request):
    return render(request, "saleshistory.html")

def newsale(request):
    return render(request, "newsale.html")

def purchasehistory(request):
    return render(request, "purchasehistory.html")

def newpurchase(request):
    return render(request, "newpurchase.html")


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}

    return render(request,'error_404.html',data)
