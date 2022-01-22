from django.contrib import admin
from .models import Stock,Rate,Party,Product,Invoice,Invoice_item
# Register your models here.
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Rate)
admin.site.register(Party)
admin.site.register(Invoice)
admin.site.register(Invoice_item)



