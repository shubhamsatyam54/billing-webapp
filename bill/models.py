from datetime import date
from django.core.exceptions import ValidationError
from ajax_select.fields import AutoCompleteField
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
    quantity = models.PositiveIntegerField(blank=False)
    M_date = models.DateField(blank=False)
    E_date = models.DateField(blank=False)

    def __str__(self):
        return f"{self.quantity}"


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

class Purchase(models.Model):
    Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True,blank=False)
    date = models.DateField(default=date.today)
    prod_quan = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    id = models.AutoField(primary_key=True)

class PurchaseItems(models.Model):
    invoice_number=models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True,blank=False)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(blank=False)
    #batch = models.ForeignKey(Batch,to_field='batch',on_delete=models.SET_NULL, null=True,blank=False)
    batch = ChainedForeignKey(
        Batch,
        chained_field="product",
        chained_model_field="product",
        show_all=False,
        auto_choose=False,
        default=None)
    rate = models.FloatField(blank=False)





class Sales(models.Model):
    invoice_id = models.AutoField(max_length=50,auto_created=True, primary_key=True, blank=False,default="1")
    date=models.DateField(default=date.today)
    total = models.FloatField()
    gst = models.FloatField()
    discount = models.FloatField(null=True)
    round = models.FloatField(null=True)
    g_total = models.FloatField()



class Salesitem(models.Model):
    """def quan_vali(self,):

        result = Stock.objects.filter(pro_batch=self.batch)[0].quantity
        if self.quan >= result :
            return self.quan
        else:
            raise ValidationError("Entered quantity is less than available quantity")"""

    invoice_id = models.ForeignKey(Sales, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    batch = ChainedForeignKey(
        Batch,
        chained_field="product",
        chained_model_field="product",
        show_all=False,
        auto_choose=False,
        default=None)
    quan = models.IntegerField(null=True,blank=False,)
    rate = models.DecimalField(decimal_places=2,max_digits=9)
    cost = models.FloatField(default=0)
    igst = models.FloatField(null=True,blank=True)
    cgst = models.FloatField(null=True,blank=True)
    sgst = models.FloatField(null=True,blank=True)

    def get_cost(self):
        result = self.rate*self.quan
        return result

    def save(self, *args, **kwargs):
        self.cost=self.get_cost()
        super(Salesitem,self).save(*args,**kwargs)

    def __str__(self):
        return f"{self.cost}"



