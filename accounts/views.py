from django.contrib.auth import login
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import AccountsSerializer, LoginSerializer, Token


class ResgisterViewSet(viewsets.ViewSet):
    
    permission_classes = [AllowAny]
    
    def create(self, request):
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            
            return Response(data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(viewsets.ViewSet):
    
    permission_classes = [AllowAny]
    
    def create(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
        
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)