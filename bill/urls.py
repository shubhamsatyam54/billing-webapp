from . import views
from django.urls import path

urlpatterns = [
    path("",views.dashboard,name="dashboard"),
    path("stock", views.stock, name="stock"),
    path("saleshistory", views.saleshistory, name="saleshistory"),
    path("newsales", views.newsale, name="newsales"),
    path("purchasehistory", views.purchasehistory, name="purchasehistory"),
    path("newpurchase", views.newpurchase, name="newpurchase"),


]
