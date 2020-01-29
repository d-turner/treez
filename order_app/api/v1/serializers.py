# -*- coding: utf-8 -*-
import logging
from rest_framework import serializers

from order_app import models as OrderModels


logger = logging.getLogger(__name__)


class StoreSerializer(serializers.ModelSerializer):

    items = serializers.SerializerMethodField()

    class Meta:
        model = OrderModels.Store
        fields = ['id', 'name', 'items']

    def get_items(self, obj):
        inventory_items = OrderModels.InventoryItem.objects.filter(store=obj)
        return InventoryItemSerializer(inventory_items, many=True).data


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModels.InventoryItem
        fields = ['name', 'description', 'currency', 'amount', 'quantity_available']


class OrderSerializer(serializers.ModelSerializer):

    purchased_items = serializers.SerializerMethodField()

    class Meta:
        model = OrderModels.Order
        fields = ['id', 'customer_email', 'created_at', 'checked_out_at', 'status', 'purchased_items']

    def get_purchased_items(self, obj):
        inventory_items = OrderModels.PurchasedItem.objects.filter(order=obj)
        return InventoryItemSerializer(inventory_items, many=True).data
