from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *



urlpatterns =[

    # api endpoint
    path('', LoginAPIView.as_view(), name="users"),
]
