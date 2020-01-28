# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

from django.db import models as DjangoModels

from order_app import choices as OrderChoices

logger = logging.getLogger(__name__)

# This should go in helper/const files
ROUNDED_DIGITS = 8
ROUNDED_DECIMALS = 2


##########
# Models #
##########
class Store(DjangoModels.Model):

    name = DjangoModels.CharField(max_length=255)
    items = DjangoModels.ManyToManyField('InventoryItem', related_name='stores')

    class Meta(object):
        db_table = u'orders_store'

    def __str__(self):
        return u'#{id} Store - {name}'.format(
            id=self.id,
            name=self.name
        )


class InventoryItem(DjangoModels.Model):

    CURRENCY = OrderChoices.CURRENCY_CHOICES
    name = DjangoModels.CharField(max_length=255)
    description = DjangoModels.TextField(blank=True, null=True)
    currency = DjangoModels.CharField(max_length=4, choices=CURRENCY)
    amount = DjangoModels.DecimalField(
        max_digits=ROUNDED_DIGITS,
        decimal_places=ROUNDED_DECIMALS
    )
    quantity_available = DjangoModels.PositiveIntegerField(default=0)

    class Meta(object):
        db_table = u'orders_item'

    def __str__(self):
        return u'#{id} InventoryItem - {name}'.format(
            id=self.id,
            name=self.name
        )


class Order(DjangoModels.Model):
    
    STATUS = OrderChoices.ORDER_STATUS_CHOICES
    customer_email = DjangoModels.EmailField(max_length=255, verbose_name='Email Address', null=False, blank=False)
    created_at = DjangoModels.DateTimeField(auto_now_add=True)
    checked_out_at = DjangoModels.DateTimeField(null=True, blank=True)
    status = DjangoModels.CharField(max_length=4, choices=STATUS)

    class Meta(object):
        db_table = u'orders_order'

    def __str__(self):
        return u'#{id} Order - {user}'.format(
            id=self.id,
            user=self.customer_email
        )
