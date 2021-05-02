from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """ 
    The following Usermanager class is created to create 2 differnet users
    1) normal user 
    2) admin user 

    """

    def create_user(self, **kwargs):
        """ Genereal user is created wthout admin status  """

        # kwargs['password'] = make_password(kwargs['password'])
        password = kwargs.pop("password")
        user = self.model(**kwargs)
        user.set_password(password)
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, **kwargs):
        """ user created with admin status """

        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.save()
        return user
