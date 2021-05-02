import uuid

# django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
# rest
from rest_framework_simplejwt.tokens import RefreshToken
# importing the usermanager
from .manager import UserManager


class User(AbstractUser):
    username=None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    phone = models.TextField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    USERNAME_FIELD = 'phone'
    objects = UserManager()

    class Meta:
        ordering = ["phone"]
        unique_together = ("name", "phone")

    def __str__(self):
        return self.phone + self.name
    
    

    