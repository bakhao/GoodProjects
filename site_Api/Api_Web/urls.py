from django.urls import path, include
from . import  views
from rest_framework import  routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()

router.register('employees', views.employeeList)

urlpatterns = [
   path('', include(router.urls)),
]