# -*- coding: utf-8 -*-
"""treez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from django.conf.urls import url, include

from order_app.api.v1 import viewsets as OrderViewSets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()


#############
# User APIs #
#############
router.register(r'users', UserViewSet)


#############
# Order APIs #
#############
router.register(r'inventories/items', OrderViewSets.InventoryItemViewSet)
router.register(r'inventories', OrderViewSets.StoreViewSet)
router.register(r'orders', OrderViewSets.OrderViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url('admin/', admin.site.urls),
]
