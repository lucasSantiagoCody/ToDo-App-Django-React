from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoRegisterSerializer, TodoSerializer
from rest_framework.authentication import SessionAuthentication
from .models import ToDo

class TodoRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        request.data['user'] = request.user.id
        serializer = TodoRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            
            todo = serializer.save()
            if todo:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class TodoListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.is_authenticated:
            todos = ToDo.objects.filter(user=request.user)

            serializer = TodoSerializer(todos, many=True)

            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

