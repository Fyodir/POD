from django.contrib import admin

# Register your models here.
from catalogue.models import *

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')

@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'minimum', 'maximum')

@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
        list_display = ('name', 'location')

@admin.register(ProductInstance)
class ProductInstanceAdmin(admin.ModelAdmin):
    list_display = ('product_type', 'id', 'team', 'storage', 'stock', 'minimum_stock')

class ProductInstanceInline(admin.TabularInline):
    model = ProductInstance

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier', 'price', 'product_EROS')
    # inlines = [ProductInstanceInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_type', 'quantity', 'team', 'requisition_id', 'urgency', 'order_status', 'date_created', 'date_delivered', 'orderer')

class OrderInline(admin.TabularInline):
    model = Order

@admin.register(Requisition)
class RequisitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'req_ref', 'requisition_status', 'date_created', 'date_sent',)
    inlines = [OrderInline]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [ProductInstanceInline]
