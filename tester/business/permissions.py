from rest_framework import permissions
from tester.sample.models import User
class IsOwner(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        try:
            decoded_token = jwt.decode(auth_token,options={"verify_signature":False})
        except (jwt.DecodeError,jwt.InvalidAlgorithmError):
            raise exceptions.AuthenticationFailed('Bad Token')
        
        phone = decoded_token['phone_number']
        u = User.objects.filter(phone=phone)
        
        uuid = u[0].id
        print("permissions")
        print(uuid)
        print(obj.owner)
        return obj.owner == uuid
