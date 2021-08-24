
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
    return Response({"message":"This is easyposi users api."})

class BussinessViewSet(viewsets.ModelViewSet):

    queryset =  Bussiness.objects.all()
    serializer_class = BussinessSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



