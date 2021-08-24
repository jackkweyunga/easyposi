
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def api_root(request):
    return Response({"message":"This is easyposi api."})

class ItemViewSet(viewsets.ModelViewSet):

    queryset =  Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class SaleViewSet(viewsets.ModelViewSet):
    
    queryset =  Sale.objects.all()
    serializer_class = SaleSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class EntryViewSet(viewsets.ModelViewSet):
    
    queryset =  Entry.objects.all()
    serializer_class = EntrySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



