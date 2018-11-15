from rest_framework import serializers
from .models import IFSC

class ApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = IFSC
        fields = ('id','ifsc_code','bank_name','city','branch_name','address')