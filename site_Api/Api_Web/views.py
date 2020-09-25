from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from .serializers import employeesSerializer
from .models import employees

from rest_framework import viewsets


class employeeList(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = employeesSerializer
