from django.db import models

# Create your models here.
from django.db import models

from django.core.exceptions import ValidationError
from django.db import models

from tester.common.models import BaseModel, BaseModelWithOutPrimaryKey
from tester.sample.models import User





class Business(BaseModel):
    """
    Imported Base class from common app
    custom error message for unique
    """

    CATEGORY=[
        ('KIRANA','KIRANA'),
        ('MEDICAL','MEDICAL'),
        ('HARDWARE','HARDWARE')
    ]

    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = models.TextField()
    business_type = models.CharField(choices=CATEGORY,max_length=255)

    class Meta:
        ordering = ["-created_at"]


class Employee(BaseModel):
    """
    Imported Base class from common app
    """

    business = models.ForeignKey(to=Business,on_delete = models.CASCADE)
    name = models.CharField(max_length=254)
    age = models.IntegerField(max_length=254)
    salary = models.IntegerField(max_length=500)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True,
                             blank=True)
    class Meta:
        ordering =["-created_at"]

class Attendance(BaseModel):

    emp = models.ForeignKey(to=Employee,on_delete= models.CASCADE)
    date = models.DateField()
    status = models.IntegerField(max_length=255)

    class Meta:
        ordering = ['-created_at']
        unique_together = ("emp", "date")
        
