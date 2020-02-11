from rest_framework import serializers
from .models import UserData

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserData
        fields=('id','first_name','last_name','company_name','age','city','state','zip','email','web')