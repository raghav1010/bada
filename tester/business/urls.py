from django.urls import path
# from . import views


# urlpatterns =[
#      path('',views.BusinessListAPIView.as_view(),name ="Business"),
#      path('<int:id>',views.BusinessDetailAPIView.as_view(),name ="Business"),
# ]

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'Business', BusinessViewSet, basename="Business")
router.register(r'Employee',EmployeeView,basename="Employee")

urlpatterns = router.urls 
