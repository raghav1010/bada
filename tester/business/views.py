from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .serializers import BusinessSerializer, EmployeeSerializer, AttendanceSerializer
from .models import Business
from .permissions import IsOwner
import jwt
from tester.sample.models import User
from .models import Business, Employee, Attendance
from rest_framework.decorators import action,api_view
from rest_framework import mixins,viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
import datetime
import json

class BusinessViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet,
                   APIView):

    
    
    queryset = Business.objects.all() 

    serializer_class = BusinessSerializer

    def perform_create(self,serializer):
        
        
        print("p1")
        auth_token = self.request.user 
        try:
            decoded_token = jwt.decode(auth_token,options={"verify_signature":False})
        except (jwt.DecodeError,jwt.InvalidAlgorithmError):
            raise exceptions.AuthenticationFailed('Bad Token')
        
        phone = decoded_token['phone_number']
        u = User.objects.filter(phone=phone)
        
        uuid = u[0].id
        return serializer.save(owner=u[0])

    def get_queryset(self):
        
        print("p2")
        auth_token= self.request.user 
        try:
            decoded_token = jwt.decode(auth_token,options={"verify_signature":False})
        except (jwt.DecodeError,jwt.InvalidAlgorithmError):
            raise exceptions.AuthenticationFailed('Bad Token')
        
        phone = decoded_token['phone_number']
        u = User.objects.filter(phone=phone)
        print(u[0].id)
        uuid = u[0].id
        return self.queryset.filter(owner=u[0])
    


    @action(methods=['post', "get"], detail=True, url_name="add_employee")
    def employee(self, request, pk=None):
        
        auth_token = self.request.user 
        try:
            decoded_token = jwt.decode(auth_token,options={"verify_signature":False})
        except (jwt.DecodeError,jwt.InvalidAlgorithmError):
            raise exceptions.AuthenticationFailed('Bad Token')
        
        phone = decoded_token['phone_number']
        u = User.objects.filter(phone=phone)
        
        if request.method == "GET":
            try:
                serializer_data = EmployeeSerializer(
                    Employee.objects.filter(business_id=pk), many=True)
                return Response(serializer_data.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"detail": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "POST":
            
            try:
                
                Employee.objects.create(user=u[0],business_id=pk,name=request.data["name"],salary=request.data["salary"],age=request.data["age"])
                return Response({"detail": "successfully added employee"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"detail": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
            

        else:
            return Response({"detail": "Please request a valid method"}, status=status.HTTP_404_NOT_FOUND)


class EmployeeView(viewsets.ViewSet):
    
    permissions = (IsOwner,)

    def retrieve(self, request,pk=None):
        # do your customization here

        auth_token = self.request.user 
        try:
            decoded_token = jwt.decode(auth_token,options={"verify_signature":False})
        except (jwt.DecodeError,jwt.InvalidAlgorithmError):
            raise exceptions.AuthenticationFailed('Bad Token')
        
        phone = decoded_token['phone_number']
        u = User.objects.filter(phone=phone)

        queryset = Employee.objects.all()
        emp = queryset.filter(id=pk)
        serializer = EmployeeSerializer(emp[0])
        return Response(serializer.data)


    @action(methods=['post', "get"], detail=True, url_name="add_attendance")
    def attendance(self, request, pk=None):
        
        auth_token = self.request.user 
        try:
            decoded_token = jwt.decode(auth_token,options={"verify_signature":False})
        except (jwt.DecodeError,jwt.InvalidAlgorithmError):
            raise exceptions.AuthenticationFailed('Bad Token')
        
        phone = decoded_token['phone_number']
        u = User.objects.filter(phone=phone)
        
        if request.method == "GET":
            try:
                queryset = Attendance.objects.filter(emp_id=pk).all()
                l = request.data["startdate"].split("-")
                start_date = datetime.date(int(l[0]),int(l[1]),int(l[2]))
                l2 = request.data["enddate"].split("-")
                end_date = datetime.date(int(l2[0]),int(l2[1]),int(l2[2]))
                delta = datetime.timedelta(days=1)
                ans={"date":"status"}
                while start_date<=end_date:
                    if len(list(Attendance.objects.filter(date=start_date,emp=pk).values('date','status')))==0:
                        return Response({"detail":"Please enter dates in valid range"},status=status.HTTP_400_BAD_REQUEST)
                    dd = list(Attendance.objects.filter(date=start_date,emp=pk).values('date','status'))[0]['date']
                    ss = list(Attendance.objects.filter(date=start_date,emp=pk).values('date','status'))[0]['status']
                    ans[str(dd)]=ss
                    start_date=start_date+delta
                return Response(ans, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"detail": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


        elif request.method == "POST":
            try:
                
                Attendance.objects.create(emp_id=pk,date = request.data["date"],status=request.data["status"])
                return Response({"detail": "successfully added attendance"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"detail": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
            

        else:
            return Response({"detail": "Please request a valid method"}, status=status.HTTP_404_NOT_FOUND)