from rest_framework import serializers
from .models import *


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= Item
        fields = '_all_'

class SaleSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model= Sale
        fields = '_all_'

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model= Entry
        fields = '_all_'



        