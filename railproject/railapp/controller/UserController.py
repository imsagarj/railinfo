from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.core.files.storage import FileSystemStorage

class UserController():
    def userSignup(self,userInfo):
        print("INSIDE CONTROLLER")
        user = User()
        user.first_name = userInfo['fname']
        user.last_name = userInfo['lname']
        user.email = userInfo['email']
        user.username = userInfo['email']
        user.set_password(userInfo.get('pass'))
        user.is_active = False
        user.save()
        return user


       

      
   