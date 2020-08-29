from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class Productview(ModelViewSet):
    queryset =  Product.objects.all()
    serializer_class = Productser
