# -*- coding: utf-8 -*-
import logging
from rest_framework import viewsets, exceptions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from order_app.api.v1 import serializers as OrderSerializers
from order_app import choices as OrderChoices
from order_app import models as OrderModels

logger = logging.getLogger(__name__)


class StoreViewSet(viewsets.ModelViewSet):
    queryset = OrderModels.Store.objects.all()
    serializer_class = OrderSerializers.StoreSerializer

    @action(detail=True, methods=['GET'])
    def items(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response(
            OrderSerializers.InventoryItemSerializer(
                obj.items.all(),
                many=True,
            ).data,
            status=status.HTTP_200_OK
        )


class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = OrderModels.InventoryItem.objects.all()
    serializer_class = OrderSerializers.InventoryItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderModels.Order.objects.all()
    serializer_class = OrderSerializers.OrderSerializer

    def create(self, request):
        inventories = request.data.get('inventories')
        purchased_items = []
        if inventories and isinstance(inventories, list):
            for inventory in inventories:
                inventory_item = OrderModels.InventoryItem.objects.get(id=inventory)
                if inventory_item.quantity_available <= 0:
                    return exceptions.ParseError()
                inventory_item.quantity_available = inventory_item.quantity_available - 1
                inventory_item.save()
                purchased_item = OrderModels.PurchasedItem.objects.create(
                    name=inventory_item.name,
                    description=inventory_item.description,
                    currency=inventory_item.currency,
                    amount=inventory_item.amount,
                    quantity=1,
                )
                purchased_items.append(purchased_item.id)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        for purchased_item_id in purchased_items:
            purchased_item = OrderModels.PurchasedItem.objects.get(id=purchased_item_id)
            purchased_item.order = order
            purchased_item.save()
        order.status = dict(OrderChoices.ORDER_STATUS_CHOICES)['CP']
        order.save()
        return Response(serializer.data)
