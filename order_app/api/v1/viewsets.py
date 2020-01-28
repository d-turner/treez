# -*- coding: utf-8 -*-
import logging
from rest_framework import viewsets

from order_app.api.v1 import serializers as OrderSerializers
from order_app import models as OrderModels

logger = logging.getLogger(__name__)


class StoreViewSet(viewsets.ModelViewSet):
    queryset = OrderModels.Store.objects.all()
    serializer_class = OrderSerializers.StoreSerializer


class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = OrderModels.InventoryItem.objects.all()
    serializer_class = OrderSerializers.InventoryItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderModels.Order.objects.all()
    serializer_class = OrderSerializers.OrderSerializer
