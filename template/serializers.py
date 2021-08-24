from rest_framework import serializers
from .models import *


class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model= Template
        fields = '_all_'