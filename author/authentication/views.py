from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets  
from django.http import JsonResponse
from rest_framework.decorators import api_view 
# from rest_framework.authentication import BasicAuthentication
# from rest_framework .permissions import IsAuthenticated

# Create your views here.

class Studentviewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
     
    serializer_class=StudentSerializers 
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]