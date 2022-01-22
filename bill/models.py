from django.db import models


# Create your models here.

class Product(models.Model):
    pro_id = models.CharField(max_length=50, primary_key=True, blank=False)
    pro_name = models.CharField(max_length=300)
    avil_quant = models.IntegerField()


class Stock(models.Model):
    pro_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    pro_batch = models.CharField(max_length=50)
    quantity = models.IntegerField()
    M_date = models.DateField()
    E_date = models.DateField()


class Party(models.Model):
    name = models.CharField(max_length=300, primary_key=True)
    add = models.TextField()


class Rate(models.Model):
    pro = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    rt_name = models.CharField(max_length=20, default="default")
    cost = models.FloatField(blank=False)


class Invoice(models.Model):
    invoice_id = models.CharField(max_length=50, primary_key=True, blank=False)
    total = models.FloatField()
    gst = models.FloatField()
    discount = models.FloatField(null=True)
    round = models.FloatField(null=True)
    g_total = models.FloatField()


class Invoice_item(models.Model):
    invoice_id = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    rate = models.ForeignKey(Rate, to_field='rt_name', on_delete=models.SET_NULL, null=True)


