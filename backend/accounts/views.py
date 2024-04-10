from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from .serializers import UserSerializer, UserLoginSerializer
from .models import CustomUser
from rest_framework.response import Response
from django.contrib.auth import login, logout
from .validations import custom_validation
import json


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):

        request_data = custom_validation(request.data)

        if request_data['errors']:
            
            errors = json.dumps({
                'errors': request_data['errors']
            })

            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            serializer = UserSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.check_user(data=request.data)
            if user:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [SessionAuthentication]

    def post(self, request):
        try:
            logout(request)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

