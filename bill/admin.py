from django.contrib import admin
from .models import Stock, Rate, Party, Product, Sales, Salesitem, Purchase,PurchaseItems, Batch


# Register your models here.
class StockV(admin.ModelAdmin):
    # admin.site.index="hey"
    list_display = ['pro', 'pro_batch', 'quantity', 'M_date', 'E_date']

class purchase_items(admin.TabularInline):
    model = PurchaseItems

class PurchaseV(admin.ModelAdmin):
    inlines = [purchase_items, ]

class sales_items(admin.TabularInline):
    model = Salesitem
    readonly_fields = ['sgst', 'igst', 'cgst',]

    #readonly_fields =

    def sgst(self,rate):
        return rate*2

class sales(admin.ModelAdmin):

    inlines = [sales_items, ]


class ProductV(admin.ModelAdmin):
    list_display = ['pro_id', 'pro_name', 'Available_Quantity']

    def Available_Quantity(self, pro_id):
        from django.db.models import Sum
        result = Stock.objects.filter(pro=pro_id).aggregate(Sum("quantity"))
        return result['quantity__sum']


"""class PurchaseV(admin.ModelAdmin):
    
        def formfield_for_foreignkey(self, db_field, request, **kwargs):
            if db_field.name == "batch":
                kwargs["queryset"] = Batch.objects.filter(product='product')
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
"""

admin.site.register(Product, ProductV)
admin.site.register(Stock, StockV)
admin.site.register(Rate)
admin.site.register(Party)
admin.site.register(Sales, sales)
admin.site.register(Salesitem)
admin.site.register(Purchase, PurchaseV)
admin.site.register(PurchaseItems)
admin.site.register(Batch)
