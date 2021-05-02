from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework import status

class LoginAPIView(GenericAPIView):
    # permission_classes = (IsAuthenticated,)  # Must include it to test user is authenticated 
    
    def post(self, request, *args, **kwargs): # will get user instance 
        serializer_class = UserSerializer
        
        data = serializer_class.validate(auth_token=request.user)
        return Response(data,status=status.HTTP_200_OK) 

# DRF settings

    