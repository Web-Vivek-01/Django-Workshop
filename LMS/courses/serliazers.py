from rest_framework import serializers
from .models import *

class lmsSignupSerliazer(serializers.Serializer):
    userName = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    number = serializers.CharField(max_length=10)  
    userType = serializers.CharField(max_length=20)
    gender = serializers.CharField(max_length=20, allow_null=True, allow_blank=True)


class lmsUpdateEmailSerliazer(serializers.Serializer):
    email = serializers.EmailField()
    number = serializers.CharField()  


class lmsDeleteUserByEmailSerliazer(serializers.Serializer):
    email = serializers.EmailField()