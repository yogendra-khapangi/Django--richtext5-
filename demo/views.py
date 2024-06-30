from django.shortcuts import render

# Create your views here.
from .models import *
from rest_framework import viewsets
from .serializer import *

class StudentModelviewset(viewsets.ModelViewSet):
    queryset = contactModel.objects.all()
    serializer_class=SudentSerializer