"""Custom authentication module"""


import jwt 
import uuid 
from django.conf import settings
from .models import User
from django.utils.translation import ugettext_lazy as _
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.exceptions import AuthenticationFailed
import random


class CustomAuthentication(BaseAuthentication):
    """
    Custom authentication class.
    It will authenticate any incoming request
    as the user given by the FireBase Token in a
    custom request header.
    """

    def authenticate(self, request):
        """
        Returns a `User` if a correct FireBase has been supplied
        using HTTP Basic authentication.  Otherwise returns `None`.
        """

        # Gets authorization from request header
        # and checks different possibility of
        # invalid header.
        # ======================================
        if request.get_full_path().find("swagger")!=-1:
            return ("swagger",None)
        auth = self.get_authorization_header(request)
        val = auth.split(".")
        # print(val)
        if not val :
            raise AuthenticationFailed(("Invalid header!"))

        if len(val) == 1:
            msg = _("Invalid basic header. No credentials provided.")
            raise AuthenticationFailed(msg)
        elif len(val) == 2:
            msg = _(
                "Invalid basic header. Credentials string should not contain two segments."
            )
            raise AuthenticationFailed(msg)

        return (auth,None)

        # try:
        #     decoded_token = jwt.decode(auth,options={"verify_signature":False})
        # except (jwt.DecodeError,jwt.InvalidAlgorithmError):
        #     raise exceptions.AuthenticationFailed('Bad Token')
        
        # phone = decoded_token['phone_number']
        # name =""
        
        # An user object is expected to be returned
        # in case of successful authentication. Therefore
        # a user object is returned with the given user_id 
        # and phone in the header. 
        # ===============================================


        # user = User.objects.filter(phone=phone)
        # print("-------------------------------")
        # print(user)
        # if user.exists():
        #     print("Already Existing User")
        #     return (user,None)
            
        # else:
        #     random_password = str(random.randint(0, 1000))
            
        #     new_user = User.objects.create(name=name,phone=phone, password=random_password)
        #     print("New User")
            # return (new_user, None)

    @staticmethod
    def get_authorization_header(request):
        """
        Return request's 'Authorization:' header, as a bytestring.
        """
        request.get_full_path()
        auth = request.META.get("HTTP_AUTHORIZATION", "").replace("Bearer ", "")
        # print(auth)
        return auth