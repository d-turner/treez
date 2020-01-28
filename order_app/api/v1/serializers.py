# -*- coding: utf-8 -*-
import logging
from rest_framework import serializers

from order_app import models as OrderModels


logger = logging.getLogger(__name__)


class StoreSerializer(serializers.ModelSerializer):

    items = serializers.SerializerMethodField()

    class Meta:
        model = OrderModels.Store
        fields = ['name', 'items']

    def get_items(self, obj):
        return 'halp'


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModels.InventoryItem
        fields = ['name', 'description', 'currency', 'amount', 'quantity_available']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModels.Order
        fields = ['customer_email', 'created_at', 'checked_out_at', 'status']
