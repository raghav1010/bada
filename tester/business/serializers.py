from rest_framework import serializers
from .models import Business,Employee,Attendance

class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = ['name','description','business_type','id']


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id','name','age','salary','business']
        depth = 1 

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ['date','status']