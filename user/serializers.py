from rest_framework import serializers
from .models import *


class BussinessSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= Bussiness
        fields = '_all_'