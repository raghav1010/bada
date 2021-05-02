from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError
import jwt
from django.conf import settings
from .models import User

import random
class UserSerializer(serializers.Serializer):
    """
            Creates a User
    """
    
    def validate(auth_token):
        
        # print(auth_token)

        try:
            decoded_token = jwt.decode(auth_token,options={"verify_signature":False})
        except (jwt.DecodeError,jwt.InvalidAlgorithmError):
            raise AuthenticationFailed('Invalid Token')
        
        phone = decoded_token['phone_number']
        name=""
        user = User.objects.filter(phone=phone)
        try:
            if user.exists():
                
                return {"phone":phone}
            else:
                
                random_password = str(random.randint(0, 1000))
                new_user = User.objects.create(name=name,phone=phone, password=random_password)
                
                return {"phone":phone}
        except Exception as e:
            raise e

        return user
        


