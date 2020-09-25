

from rest_framework import serializers
from .models import employees

class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = ['id','firstname','lastname','emp_id']
