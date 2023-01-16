from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Item,Location


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')