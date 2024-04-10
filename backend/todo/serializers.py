from rest_framework import serializers 
from .models import ToDo
from .validations import validate_data_of_request
from accounts.models import CustomUser

class TodoRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['user', 'title', 'description', 'status', 'priority', 'created_at']



class TodoSerializer(serializers.ModelSerializer):
    class  Meta:
        model = ToDo
        fields = '__all__'