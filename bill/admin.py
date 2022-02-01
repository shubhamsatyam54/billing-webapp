from django.contrib import admin
from .models import Stock,Rate,Party,Product,Invoice,Invoice_item,Purchase,Batch
# Register your models here.
class StockV(admin.ModelAdmin):
    #admin.site.index="hey"
    
    list_display = ['pro','pro_batch','quantity','M_date','E_date']


class items(admin.TabularInline):
    model = Invoice_item
    readonly_fields = ['sgst','igst','cgst']


class InvoiceV(admin.ModelAdmin):
    list_display = ['invoice_id']
    inlines = [items,]


class PurchaseV(admin.ModelAdmin):
    list_display = ['invoice_id']
    inlines = [items,]


class ProductV(admin.ModelAdmin):
    list_display = ['pro_id','pro_name','Available_Quantity']

    def Available_Quantity(self, pro_id):
        from django.db.models import Sum
        result = Stock.objects.filter(pro=pro_id).aggregate(Sum("quantity"))
        return result['quantity__sum']

class PurchaseV(admin.ModelAdmin):\

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "batch":
            kwargs["queryset"] = Batch.objects.filter(product='product')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Product,ProductV)
admin.site.register(Stock,StockV)
admin.site.register(Rate)
admin.site.register(Party)
admin.site.register(Invoice,InvoiceV)
admin.site.register(Invoice_item)
admin.site.register(Purchase,PurchaseV)
admin.site.register(Batch)




