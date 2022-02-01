from datetime import date

from django.db import models
from smart_selects.db_fields import GroupedForeignKey , ChainedForeignKey , ChainedManyToManyField


# Create your models here.

class Product(models.Model):
    pro_id = models.CharField(max_length=50, primary_key=True, blank=False)
    pro_name = models.CharField(max_length=300)
    def __str__(self):
        return f"{self.pro_name}"
class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=False)
    batch = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return f"{self.batch}"


class Stock(models.Model):
    pro = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=False)
    pro_batch = models.ForeignKey(Batch,to_field='batch',on_delete=models.SET_NULL, null=True,blank=False)
    quantity = models.IntegerField(blank=False)
    M_date = models.DateField(blank=False)
    E_date = models.DateField(blank=False)

    def __str__(self):
        return f"{self.pro_batch}"


class Party(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    add = models.TextField(blank=False)

    def __str__(self):
        return f"{self.name}"


class Rate(models.Model):
    pro = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=False)
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True,blank=False)
    rt_name = models.CharField(max_length=20, default="default")
    cost = models.FloatField(blank=False)


class Invoice(models.Model):
    invoice_id = models.CharField(max_length=50,auto_created=True, primary_key=True, blank=False,default="1")
    date=models.DateField(default=date.today)
    total = models.FloatField()
    gst = models.FloatField()
    discount = models.FloatField(null=True)
    round = models.FloatField(null=True)
    g_total = models.FloatField()


class Purchase(models.Model):

    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(blank=False)
    #batch = models.ForeignKey(Batch,to_field='batch',on_delete=models.SET_NULL, null=True,blank=False)
    batch = ChainedForeignKey(
        Batch,
        chained_field="product",
        chained_model_field="product",
        show_all=False,
        auto_choose=False,
        default=None)
    rate = models.FloatField(blank=False)

    def __str__(self):
        return f"{self.product}"


class Invoice_item(models.Model):
    invoice_id = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quan = models.IntegerField(null=True,blank=False)
    rate = models.FloatField()
    cost = models.FloatField()
    igst = models.FloatField(null=True)
    cgst = models.FloatField(null=True)
    sgst = models.FloatField(null=True)


