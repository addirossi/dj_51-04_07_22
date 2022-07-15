from django.contrib import admin

# Register your models here.
from .models import Product, Order, OrderItems


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

