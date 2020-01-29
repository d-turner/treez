# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from order_app import models as OrderModels


class StoreAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    raw_id_fields = ('items',)


class InventoryItemAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'currency',)
    search_fields = ('id', 'name', 'description', 'currency',)


class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'customer_email', 'status',)
    search_fields = ('id', 'customer_email',)


admin.site.register(OrderModels.Store, StoreAdmin)
admin.site.register(OrderModels.InventoryItem, InventoryItemAdmin)
admin.site.register(OrderModels.Order, OrderAdmin)
admin.site.register(OrderModels.PurchasedItem)
