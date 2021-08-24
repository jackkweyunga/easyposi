from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *

# Create your views here.


class TemplateViewSet(viewsets.ModelViewSet):
    
    queryset =  Template.objects.all()
    serializer_class = TemplateSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]