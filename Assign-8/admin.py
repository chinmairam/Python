from django.contrib import admin

from .models import Store, Product, Sales

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'state', 'country')
    list_filter = ('country',)
    ordering = ('country', 'state')
    search_fields = ('store_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'brand', 'category')
    list_filter = ('category',)
    ordering = ('brand',)
    search_fields = ('product_name',)

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('date','store_id','product_id','units_sold')
    list_filter = ('date',)
    ordering = ('date','product_id','store_id')
    
